from fastapi import FastAPI
from pydantic import BaseModel
from Conversational_agent import Conv_agent

app = FastAPI()

conv = Conv_agent()

class prompt(BaseModel):
    user_prompt : str


@app.get("/gpt/prompt")
async def Post_prompt(prompt : prompt):
    return {"response" : conv.conversation(prompt.user_prompt)}

