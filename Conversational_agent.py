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
            prompt = f"dame solo las tres palabras principales del texto delimitado por tres parentesis que te mande, devuelve solo tres palabras separadas por comas((({msg})))"
            res = self.gpt_conn.talk(prompt)
            triplet = res.split(",")
            self.anzo_conn.sparql.method = 'POST'
            query = f"""
                INSERT DATA
                {{
                GRAPH <TECH_SUPP>
                {{
                    _:sujeto <sujeto> "{triplet[0]}" ;
                            <verbo> "{triplet[1]}" ;
                            <predicado> "{triplet[2]}" .
                }}
                }}
            """
            self.anzo_conn.sparql.setQuery(query.encode("utf-8"))
            self.anzo_conn.sparql.setReturnFormat(JSON)

            results = self.anzo_conn.sparql.query().convert()

            if results in results:
                return 'prompt success saved in graph'
            else:
                return 'error saving prompt in graph'


# conv = Conv_agent()

# print(conv.KG_insert('como instalo windows'))