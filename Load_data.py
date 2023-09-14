import re
import glob
from langchain.document_loaders import WebBaseLoader


class LoadData:

  def __init__(self):
    self.files = glob.glob("*.txt")
    self.links = self.obtain_links(self.files)
    self.docs = self.load_data(self.links)
  
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
          
  def load_data(self, links):
    loader = WebBaseLoader(links)
    docs = loader.load()
    return docs

# loader = LoadData()
# print(loader.docs)
# print(type(loader.docs))
# print(type(loader.docs[0]))