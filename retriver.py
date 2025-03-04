from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.prompts import ChatPromptTemplate
import google.generativeai as genai
from dotenv import load_dotenv
import os
load_dotenv()

#gemini_api_key = os.getenv("GEMINI_API_KEY")


class Retriver:
    def __init__(self):
        self.embeddings = HuggingFaceEmbeddings()

        self.vector_store = FAISS.load_local(
            "faiss_index", self.embeddings,allow_dangerous_deserialization=True
             )
        
    def llm_response(self,prompt):

        genai.configure(api_key= os.getenv("GEMINI_API_KEY"))
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(prompt)

        return response.text

    def get_answer(self,query_text):
        PROMPT_TEMPLATE = """
        Answer the question based only on the following context:

        {context}

        ---
        Answer the question based on the above context: {question}

        If no relevant content is found, respond with:
        "I don't have information related to your query in the provided documents."

        """

        query_embedding = self.embeddings.embed_query(query_text)
        results = self.vector_store.similarity_search_by_vector(
            query_embedding, k=3,
        )

        for i,doc in enumerate(results):
            print(f'------- chunk-{i} ----------')
            print(f"{doc.page_content}")
            #print(f"{[{doc.metadata}]}")

        context_text = "\n\n---\n\n".join([doc.page_content for doc in results])
        prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
        prompt = prompt_template.format(context=context_text, question=query_text)

        answer = self.llm_response(prompt)
        
        print('-------- Answer ----------')
        print(answer)
        return answer

