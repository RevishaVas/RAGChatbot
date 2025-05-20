from langchain_ollama import OllamaLLM



chat = OllamaLLM(model="phi")  # Updated class name
response = chat.invoke("Tell me a joke")  # Use `invoke` instead of calling like a function
print(response)