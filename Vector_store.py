from langchain.vectorstores import Chroma
from Splitting import Splitter
from chromadb.api.types import Embeddings

db_directory = 'docs/chroma'

docs = Splitter().splitted_data
vectordb = Chroma.from_documents(documents=docs, embedding=Embeddings, persist_directory=db_directory)

print(docs)
print(type(docs))
print(type(docs[-1]))
print(type(docs[-1][0]))

print(vectordb._collection.count())