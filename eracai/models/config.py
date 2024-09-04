import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    AZURE_API_KEY = os.getenv('AZURE_API_KEY')
    AZURE_ENDPOINT = os.getenv('AZURE_ENDPOINT')
    GROQ_API_KEY = os.getenv('GROQ_API_KEY')
    ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY')
    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
    WEAVIATE_URL = os.getenv('WEAVIATE_URL')
    
    MAX_RETRIES = int(os.getenv('MAX_RETRIES', 3))
    TIMEOUT = int(os.getenv('TIMEOUT', 30))