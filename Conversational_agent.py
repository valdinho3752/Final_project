from langchain.chains import ConversationalRetrievalChain
from OpenIA_connection import GPT_connection
from Vector_store import Vector_Store
from langchain.chat_models import ChatOpenAI

vectorstore = Vector_Store().vectordb

chat = ConversationalRetrievalChain.from_llm(ChatOpenAI(temperature=0), vectorstore.as_retriever())

chat_history = []
    
def conversation(user_message, history):
    # Get response from QA chain
    response = chat({"question": user_message, "chat_history": history})
    # Append user message and response to chat history
    history.append((user_message, response["answer"]))

    return response["answer"]

conv = conversation('que es la maquina de turing', chat_history)
print(conv)