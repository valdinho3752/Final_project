from langchain.text_splitter  import RecursiveCharacterTextSplitter, CharacterTextSplitter
from Load_data import LoadData

class Splitter:

    def __init__(self):
        self.data = LoadData().docs
        self.chunk_size = 100
        self.chunk_overlap = 50
        self.r_splitter = RecursiveCharacterTextSplitter( chunk_size = self.chunk_size, chunk_overlap = self.chunk_overlap, separators=["\n", "\n\n","\n\n" * 3, " ", ""])
        self.c_splitter = CharacterTextSplitter( chunk_size = self.chunk_size, chunk_overlap = self.chunk_overlap, separator = ' ')
    
    def splitter(self, data):
        texts_splitted = []
        for doc in data:
            text = self.c_splitter.split_text(doc[0].page_content)
            texts_splitted.append(text)
        return texts_splitted
#split = Splitter()
#print(split.splitter(split.data))