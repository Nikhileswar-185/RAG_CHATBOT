# RAG_CHATBOT 
A Retrieval-Augmented Generation (RAG) chatbot built using Streamlit, LangChain, FAISS, and Hugging Face embeddings.  
This chatbot can answer user queries based on our custom data.

## 🚀 Installation  
Clone the repository and install the required dependencies.

```bash
git clone https://github.com/Nikhileswar-185/RAG_CHATBOT.git
cd RAG_CHATBOT
pip install -r requirements.txt

---

## **3️⃣ LLM Configuration**
https://www.googleadservices.com/pagead/aclk?sa=L&ai=DChcSEwi2u8DevfCLAxV2pGYCHU90DKEYABAAGgJzbQ&co=1&gclid=CjwKCAiA5pq-BhBuEiwAvkzVZTArACFSm3-ObwnnVXiM8Fh79RHV24XQmfI4FfxJwrVdpD2BD3bZTRoCGeQQAvD_BwE&ohost=www.google.com&cid=CAESVeD2hDML-cIRLTL182WcPU-i-HptWeN5u2KunU0ppHm25qvoeq7-_5WB1SXI35v5X7ZL7CBzOUfS7glS8wRIvly26rPeK2BC51ifHoqXmfguCCmJuRA&sig=AOD64_0AZcKBfjCOiRdbTR6nQbWDJjw7-w&q&adurl&ved=2ahUKEwjRqrvevfCLAxXwamwGHR4CEXQQ0Qx6BAgJEAE



## **3️⃣ How to Use**
```md
## 📖 Usage  
In the terminal,  run the below command - it creates embeddings and store them in FAISS vector database
1. python create_faiss_index.py

Once you see the message "All files processed successfully!" , run the below command
2.streamlit run app.py

Opens your chatbot in localhost




