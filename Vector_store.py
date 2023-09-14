from langchain.vectorstores import Chroma
from Splitting import Splitter
from langchain.embeddings import OpenAIEmbeddings
from OpenIA_connection import GPT_connection

db_directory = 'docs/chroma'

api_key = GPT_connection().apiKey

embeddings = OpenAIEmbeddings(openai_api_key=api_key)

docs = Splitter().splitted_data

documents = []

vectordb = Chroma.from_documents(documents=docs, embedding=embeddings, persist_directory=db_directory)


print(vectordb._collection.count())

# print(docs)
# print(type(docs))
# print(type(docs[-1]))
# print(type(docs[-1][0]))

# print(vectordb._collection.count())