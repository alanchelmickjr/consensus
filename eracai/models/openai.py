from .config import Config
from .logger import logger
from .exceptions import AIConsensusError, ModelQueryError, VotingError, DatabaseError
import openai
from .base_model import BaseModel

class OpenAIModel(BaseModel):
    def __init__(self):
        openai.api_key = "your-openai-api-key"  # Set this securely
        self._name = "OpenAI"

    @property
    def name(self):
        return self._name

    def query(self, formatted_query, max_tokens, temperature):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": formatted_query}],
            max_tokens=max_tokens,
            temperature=temperature
        )
        return response.choices[0].message['content']

    def vote_on_responses(self, responses):
        voting_prompt = "Rate each of the following responses on a scale of 1 to 10, where 10 is the best:\n\n"
        for model, response in responses.items():
            voting_prompt += f"{model}: {response}\n\n"
        voting_prompt += "Provide your ratings as a JSON object with model names as keys and ratings as values."

        vote_response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": voting_prompt}],
            max_tokens=1000,
            temperature=0.2
        )
        
        # Parse the JSON response
        import json
        return json.loads(vote_response.choices[0].message['content'])