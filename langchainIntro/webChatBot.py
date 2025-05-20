import gradio as gr
from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaLLM, OllamaEmbeddings
from langchain.chains import RetrievalQA

# Load Chroma vector store
db = Chroma(
    persist_directory="../db",
    embedding_function=OllamaEmbeddings(model="phi")
)
retriever = db.as_retriever()

# Load local LLM
llm = OllamaLLM(model="phi")

# RAG Chain
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    return_source_documents=True
)

# Chat handler
def ask_bot(question):
    if not question.strip():
        return "❗ Please ask a valid question."

    result = qa_chain.invoke(question)
    answer = result["result"]

    # Optional: Show sources
    sources = "\n\n".join([f"- {doc.page_content}" for doc in result["source_documents"]])
    return f"**Answer:** {answer}\n\n---\n"

# Gradio UI
iface = gr.Interface(
    fn=ask_bot,
    inputs=gr.Textbox(lines=2, placeholder="Ask about the hospital reviews..."),
    outputs=gr.Markdown(),
    title="🏥 Hospital Review Chatbot",
    description="Ask questions based on patient reviews from the hospital database.",
    allow_flagging="never"
)

iface.launch()
