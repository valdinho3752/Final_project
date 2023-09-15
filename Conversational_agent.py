from langchain.chains import ConversationalRetrievalChain
from Vector_store import Vector_Store
from langchain.llms import OpenAI
from SPARQLWrapper import JSON
from Anzograph_connection import Anzo_conn
from OpenIA_connection import GPT_connection

class Conv_agent:
    def __init__(self) :
        self.vectorstore = Vector_Store().vectordb

        self.anzo_conn = Anzo_conn()

        self.gpt_conn = GPT_connection()

        self.chat = ConversationalRetrievalChain.from_llm(OpenAI(temperature=0), self.vectorstore.as_retriever())

        self.chat_history = []
        
    def conversation(self, user_message):
        response = self.chat({"question": user_message, "chat_history": self.chat_history})
        self.chat_history.append((user_message, response["answer"]))

        return response["answer"]
    
    def KG_insert(self,msg):
        if self.anzo_conn.connect():
            prompt = f"Convierta el siguiente texto delimitado por triple paréntesis en una consulta de inserción SPARQL sin ningún prefijo a un grafo llamado SOPORTE_TECNICO ((({msg})))"
            res = self.gpt_conn.talk(prompt)
            self.anzo_conn.sparql.method = 'POST'
            self.anzo_conn.sparql.setQuery(f""" {res}""".encode("utf-8"))
            self.anzo_conn.sparql.setReturnFormat(JSON)

            results = self.anzo_conn.sparql.query().convert()

            if results in results:
                return 'prompt success saved in graph'
            else:
                return 'error saving prompt in graph'


# conv = Conv_agent()

# print(conv.KG_insert('como instalo windows'))