from langchain.text_splitter  import RecursiveCharacterTextSplitter, CharacterTextSplitter
from Load_data import LoadData

data = LoadData().docs

chunk_size = 100
chunk_overlap = 50

r_splitter = RecursiveCharacterTextSplitter( chunk_size = chunk_size, chunk_overlap = chunk_overlap, separators=["\n", "\n\n", " ", ""])
c_splitter = CharacterTextSplitter( chunk_size = chunk_size, chunk_overlap = chunk_overlap, separator = ' ')

def splitter(data):
    for doc in data:
        doc = c_splitter.split_text(doc[0].__str__())
        print("\n")
    return data

print(splitter(data[0]))