import google.generativeai as genai
from dotenv import load_dotenv
import os
load_dotenv()

class LLM:
    @staticmethod        
    def generate_response(prompt):
        genai.configure(api_key= os.getenv("GEMINI_API_KEY"))
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(prompt)

        return response.text
    