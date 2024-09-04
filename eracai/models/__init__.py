from .openai import OpenAIModel
from .azure import AzureModel
from .groq import GroqModel
from .anthropic import AnthropicModel
from .gemini import GeminiModel

def get_all_models():
    return [
        OpenAIModel(),
        AzureModel(),
        GroqModel(),
        AnthropicModel(),
        GeminiModel()
    ]