from langchain.text_splitter  import RecursiveCharacterTextSplitter, CharacterTextSplitter
from Load_data import LoadData

data = LoadData().docs

chunk_size = 100
chunk_overlap = 50

r_splitter = RecursiveCharacterTextSplitter( chunk_size = chunk_size, chunk_overlap = chunk_overlap, separators=["\n", "\n\n", " ", ""])
c_splitter = CharacterTextSplitter( chunk_size = chunk_size, chunk_overlap = chunk_overlap, separator = ' ')

def splitter(data):
    texts_splitted = []
    for doc in data:
        text = c_splitter.split_text(doc[0].page_content)
        texts_splitted.append(text)
    return texts_splitted

print(splitter(data))