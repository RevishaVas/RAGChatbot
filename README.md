#  Hospital Reviews RAG Chatbot

An AI-powered chatbot built using **LangChain**, **Ollama**, **Gradio**, and **ChromaDB** that answers natural language questions by retrieving relevant insights from hospital review data.

---

##  Use Case: AI-Powered Insight from Hospital Reviews

This chatbot is designed to help **patients**, **hospital administrators**, and **healthcare analysts**:

-  Ask **natural-language questions** over patient reviews.
-  Retrieve and summarize feedback on hospital staff, hygiene, facilities, or treatment experiences.
-  Make **data-informed decisions** about care quality, staffing, or patient education.

The core idea follows a Retrieval-Augmented Generation (RAG) approach — where relevant documents are retrieved and used to ground the LLM's responses.

---

##  Features

-  **LangChain**-based RAG pipeline
-  **Ollama (local `phi` model)** — no API key or billing required
-  **ChromaDB** for local vector search
-  **Gradio** web interface
-  Built entirely offline & privacy-friendly

---


##  Gradio Web Interface
![Screenshot 2025-05-20 003843](https://github.com/user-attachments/assets/a9f4fa64-0b4b-4bdf-8994-8e25992fda69)

---

##  Project Structure

![image](https://github.com/user-attachments/assets/ffd923f3-e031-41ab-9908-92f1304f3f60)

---


##  Quickstart Guide

###  1. Install Ollama

Install Ollama from [https://ollama.com](https://ollama.com) and run the `phi` model:

```
ollama run phi
```
###  2. Set Up Environment
```
git clone https://github.com/RevishaVas/RAGChatbot.git
cd RAGChatbot
```
```
# Create virtual environment
python -m venv venv
.\venv\Scripts\activate      # On Windows

# OR
source venv/bin/activate     # On macOS/Linux
```
```
# Install dependencies
pip install -r requirements.txt
```
###  3. Build the Vector Database
```
python langchainIntro/createRetriever.py
```
This loads reviews.csv, splits the content, creates embeddings with phi, and stores them using ChromaDB.

###  4. Launch the Web Chatbot  
```
python langchainIntro/webChatBot.py
```
Your browser will open the chatbot at:
 http://localhost:7860


---
##  Example Questions to Try
"What do patients say about the staff?"

"Is the hospital safe and clean?"

"How is the experience with the doctors?"

"What reviews mention patient education?"

---
##  Notes
Make sure Ollama is running and the phi model is available.
The .env and venv/ folders are excluded from Git.
You can extend the data with more CSV records for broader coverage.

---
##  Acknowledgments
Real Python: Build a RAG Chatbot with LangChain - https://realpython.com/build-llm-rag-chatbot-with-langchain/

LangChain

Ollama

Gradio

ChromaDB
