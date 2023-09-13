import os
import openai
import sys
from dotenv import load_dotenv


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