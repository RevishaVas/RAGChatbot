from langchain_community.document_loaders import CSVLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma


Reviews_CSV_Path="../data/reviews.csv"


loader=CSVLoader(file_path=Reviews_CSV_Path, source_column="review")
documents = loader.load()

# Split the documents into smaller chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
docs=text_splitter.split_documents(documents)

embedding=OllamaEmbeddings(model="phi")
db = Chroma.from_documents(documents=docs, embedding=embedding, persist_directory="db")
db.persist()

print("Database created and persisted successfully in 'db' directory.")