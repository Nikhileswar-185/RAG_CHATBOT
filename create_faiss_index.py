# from document_chunker import DocumentChunker
# from vector_store import VectorStore

# file_path = r'C:\Users\Nikhileswar\Desktop\RAG_chatbot\data\37 Million Compilations - Investigating Novice Programming Mistakes in Large-Scale Student Data (fp1187-altadmri).pdf'
# chunker = DocumentChunker()
# extracted_text = chunker.load_documents(file_path)

# chunks = chunker.split_documents(extracted_text)

# vs = VectorStore()
# vs.add_to_faiss(chunks)

from document_chunker import DocumentChunker
from vector_store import VectorStore
import os

class CreateFAISS:
    def __init__(self,folder_path='data'):
       
        self.document_chunker = DocumentChunker()
        self.vector_store = VectorStore() 
        self.folder_path = folder_path

    def update_vectors(self): 

        # Process all supported files
        for file_name in os.listdir(self.folder_path):
            if file_name.endswith(('.pdf')):  # Process both PDF and TXT files
                file_path = os.path.join(self.folder_path, file_name)
                print(f"📄 Processing: {file_name}")

                # Load document
                pages = self.document_chunker.load_documents(file_path)

                # Split into chunks
                chunks = self.document_chunker.split_documents(pages)

                # Add to FAISS
                self.vector_store.add_to_faiss(chunks)

        print("✅ All files processed successfully!")

create_faiss = CreateFAISS()
create_faiss.update_vectors()