from .config import Config
from .logger import logger
from .exceptions import AIConsensusError, ModelQueryError, VotingError, DatabaseError
import google.generativeai as genai
from .base_model import BaseModel

class GeminiModel(BaseModel):
    def __init__(self):
        genai.configure(api_key="your-gemini-api-key")  # Set this securely
        self.model = genai.GenerativeModel('gemini-pro')
        self._name = "Gemini"

    @property
    def name(self):
        return self._name

    def query(self, formatted_query, max_tokens, temperature):
        response = self.model.generate_content(
            formatted_query,
            generation_config=genai.types.GenerationConfig(
                max_output_tokens=max_tokens,
                temperature=temperature
            )
        )
        return response.text

    def vote_on_responses(self, responses):
        voting_prompt = "Rate each of the following responses on a scale of 1 to 10, where 10 is the best:\n\n"
        for model, response in responses.items():
            voting_prompt += f"{model}: {response}\n\n"
        voting_prompt += "Provide your ratings as a JSON object with model names as keys and ratings as values."

        vote_response = self.model.generate_content(
            voting_prompt,
            generation_config=genai.types.GenerationConfig(
                max_output_tokens=1000,
                temperature=0.2
            )
        )
        
        # Parse the JSON response
        import json
        return json.loads(vote_response.text)