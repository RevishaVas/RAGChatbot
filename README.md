# 🏥 Hospital Reviews RAG Chatbot

An AI-powered chatbot built using **LangChain**, **Ollama**, **Gradio**, and **ChromaDB** that answers natural language questions by retrieving relevant insights from hospital review data.

---

## 📌 Use Case: AI-Powered Insight from Hospital Reviews

This chatbot is designed to help **patients**, **hospital administrators**, and **healthcare analysts**:

- 🔍 Ask **natural-language questions** over patient reviews.
- 🧠 Retrieve and summarize feedback on hospital staff, hygiene, facilities, or treatment experiences.
- 📊 Make **data-informed decisions** about care quality, staffing, or patient education.

The core idea follows a Retrieval-Augmented Generation (RAG) approach — where relevant documents are retrieved and used to ground the LLM's responses.

---

## ⚙️ Features

- ✅ **LangChain**-based RAG pipeline
- ✅ **Ollama (local `phi` model)** — no API key or billing required
- ✅ **ChromaDB** for local vector search
- ✅ **Gradio** web interface
- ✅ Built entirely offline & privacy-friendly

---

## 📁 Project Structure

RAGChatbot/
├── data/
│ └── reviews.csv # Hospital review data
├── langchainIntro/
│ ├── chatbot.py # LLM test
│ ├── chatWithReviews.py # CLI chatbot
│ ├── createRetriever.py # Builds vector DB from CSV
│ └── webChatBot.py # Gradio Web UI
├── requirements.txt
├── .env # (ignored)
├── .gitignore
├── README.md


---


---

## 🚀 Quickstart Guide

### ⚒️ 1. Install Ollama

Install Ollama from [https://ollama.com](https://ollama.com) and run the `phi` model:

```bash
ollama run phi




❓ Example Questions to Try
"What do patients say about the staff?"
"Is the hospital safe and clean?"
"How is the experience with the doctors?"
"What reviews mention patient education?"

⚠️ Notes
Make sure Ollama is running and the phi model is available.
The .env and venv/ folders are excluded from Git.
You can extend the data with more CSV records for broader coverage.

🙌 Acknowledgments
Real Python: Build a RAG Chatbot with LangChain
LangChain
Ollama
Gradio
