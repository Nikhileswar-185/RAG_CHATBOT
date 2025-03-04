from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader
import os
from dotenv import load_dotenv
import os
load_dotenv()


class DocumentChunker:
    def __init__(self):
        pass

    def load_documents(self,file_path):
        _, file_extension = os.path.splitext(file_path)

        if file_extension.lower() == '.pdf':
            loader = PyPDFLoader(file_path)
            pages = loader.load()
        
        elif file_extension.lower() == '.txt':
            loader = TextLoader(file_path)
            pages = loader.load()

        return pages
    
    def split_documents(self,text):
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size= int(os.getenv("CHUNK_SIZE")),
            chunk_overlap= int(os.getenv("CHUNK_OVERLAP")),
            separators=[
            ".",
            "\n\n",
        ],

        )
        splitted_docs = text_splitter.split_documents(text)
        print(f"Succecfully split document into {len(splitted_docs)} chunks !")
        return splitted_docs