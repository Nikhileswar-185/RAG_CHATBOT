from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.docstore.in_memory import InMemoryDocstore
from langchain_community.vectorstores import FAISS
import faiss
import os

class VectorStore:
    def __init__(self, index_path="faiss_index"):
        self.index_path = index_path
        self.embeddings = HuggingFaceEmbeddings()
        self.vector_store = self.load_faiss_index()


    def load_faiss_index(self):
        
        if os.path.exists(self.index_path):
            print("Loading existing FAISS index...")
            return FAISS.load_local(self.index_path, self.embeddings, allow_dangerous_deserialization=True)
        
        print("Creating a new FAISS index...")
        dim = len(self.embeddings.embed_query("test")) 
        index = faiss.IndexFlatL2(dim)

        print("Vectore store loading succesfull !")
        return FAISS(
            embedding_function=self.embeddings,
            index=index,
            docstore=InMemoryDocstore(),
            index_to_docstore_id={},
        )

    def calculate_chunk_ids(self, chunks):
        
        last_page_id = None
        current_chunk_index = 0

        for chunk in chunks:
            source = chunk.metadata.get("source", "unknown")
            page = chunk.metadata.get("page", 0)
            current_page_id = f"{source}:{page}"

            if current_page_id == last_page_id:
                current_chunk_index += 1
            else:
                current_chunk_index = 0

            chunk.metadata["id"] = f"{current_page_id}:{current_chunk_index}"
            last_page_id = current_page_id

        return chunks
        
    def add_to_faiss(self,chunks):
        
        print("Indexing the chunks ..")
        chunks_with_ids = self.calculate_chunk_ids(chunks)


        new_chunks = []
        for chunk in chunks_with_ids:
            new_chunks.append(chunk)

        if len(new_chunks):
            print('adding new chunks ..')

            new_chunk_ids = [chunk.metadata["id"] for chunk in new_chunks]
            
            try:
                self.vector_store.add_documents(new_chunks, ids=new_chunk_ids)
            except Exception as e:
                print("ERROR : Documents already exists in FAISS Index , Proceed to Ask questions")
                exit()

            print(f"Inserted new documents to FIASS: {len(new_chunks)}")
            self.vector_store.save_local("faiss_index")
            print('-'*100)
        else:
            print("✅ No new documents to add")

