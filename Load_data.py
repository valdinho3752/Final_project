import re
import glob
from langchain.document_loaders import WebBaseLoader
from langchain.document_loaders import PyPDFLoader


class LoadData:

  def __init__(self):
    self.files = glob.glob("*.txt")
    self.pdf_files = glob.glob("*.pdf")
    self.links = self.obtain_links(self.files)
    self.docs = self.load_data(self.links, self.pdf_files)
  
  def obtain_links(self, files):
      link_s = []
      for file in files:
          with open(file, 'r') as f:
              links = f.readlines()
              link_s.append(links)

      cleaned_links = []  
      for links in link_s:
          for link in links:
              cleaned_link = self.remove_special_characters(link)
              cleaned_links.append(cleaned_link)
      return cleaned_links

  def remove_special_characters(self, text):
      pattern = r'\n'
      text = re.sub(pattern, '', text)
      return text
          
  def load_data(self, links,pdf_paths):
      docs = []
      for link in links:
        loader = WebBaseLoader(link)
        doc = loader.load() 
        docs.append(doc)
      for path in pdf_paths:
        loader = PyPDFLoader(path)
        pages = loader.load()
        docs.append(pages)
      return docs