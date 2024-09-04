# models/__init__.py

from .openai import OpenAIModel
from .azure import AzureModel
from .groq import GroqModel
from .anthropic import AnthropicModel
from .gemini import GeminiModel
from .config import Config
from .logger import logger
from .exceptions import AIConsensusError, ModelQueryError, VotingError, DatabaseError

def get_all_models():
    return [
        OpenAIModel(),
        AzureModel(),
        GroqModel(),
        AnthropicModel(),
        GeminiModel()
    ]

__all__ = [
    'OpenAIModel', 'AzureModel', 'GroqModel', 'AnthropicModel', 'GeminiModel',
    'Config', 'logger', 'AIConsensusError', 'ModelQueryError', 'VotingError', 'DatabaseError',
    'get_all_models'
]