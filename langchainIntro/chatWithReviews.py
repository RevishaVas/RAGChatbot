from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaLLM, OllamaEmbeddings
from langchain.chains import RetrievalQA

# Load Chroma vector store
db = Chroma(persist_directory="../db", embedding_function=OllamaEmbeddings(model="phi"))
retriever = db.as_retriever()

# Load local LLM
llm = OllamaLLM(model="phi")

# Build RetrievalQA chain
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    return_source_documents=True
)

# Simple chat loop
print("🤖 Ask me anything about the hospital reviews (type 'exit' to quit):\n")
while True:
    query = input("🧑 You: ")
    if query.lower() in ["exit", "quit"]:
        break

    result = qa_chain.invoke(query)
    print("\n🤖 Bot:", result['result'])

    # Optional: show where the info came from
    for i, doc in enumerate(result['source_documents'], 1):
        print(f"\n📄 Source {i}:\n{doc.page_content}")

