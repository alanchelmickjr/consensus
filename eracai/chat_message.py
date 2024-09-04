# chat_message.py
from pydantic import BaseModel
from typing import Dict, Any

class ChatMessage(BaseModel):
    role: str
    content: str
    metadata: Dict[str, Any] = {}