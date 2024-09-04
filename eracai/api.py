from fastapi import FastAPI
from pydantic import BaseModel
from .main import consensus_response
from .chat_message import ChatMessage

app = FastAPI()

class Query(BaseModel):
    text: str
    max_tokens: int = 1000
    temperature: float = 0.7

@app.post("/query")
async def process_query(query: Query) -> ChatMessage:
    result = await consensus_response(query.text, query.max_tokens, query.temperature)
    return result

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)