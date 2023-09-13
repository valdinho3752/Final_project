import os
import openai
import sys
from dotenv import load_dotenv
import re
import glob
from langchain.document_loaders import WebBaseLoader
from langchain.document_loaders import PyPDFLoader


load_dotenv() # read local .env file
openai.api_key = os.getenv('OPENAI_API_KEY')

'''
import requests
import json

url = "https://api.openai.com/v1/chat/completions"

payload = json.dumps({
  "model": "gpt-3.5-turbo",
  "messages": [
    {
      "role": "user",
      "content": "que es la relatividad?"
    }
  ],
  "temperature": 0.7
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': f'Bearer {openai_api_key}'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
'''

files = glob.glob("*.txt")
pdf_files = glob.glob("*.pdf")

def obtain_links(files):
    link_s = []
    for file in files:
        with open(file, 'r') as f:
            links = f.readlines()
            link_s.append(links)

    cleaned_links = []  
    for links in link_s:
        for link in links:
            cleaned_link = remove_special_characters(link)
            cleaned_links.append(cleaned_link)
    return cleaned_links



def remove_special_characters(text):
    # Definir el patrón de salto de línea
    pattern = r'\n'

    # Utilizar la función re.sub() para eliminar los saltos de línea
    text = re.sub(pattern, '', text)

    return text
        
def load_data(links,pdf_paths):
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

links = obtain_links(files)

docs = load_data(links, pdf_files)

print(docs[-1])    