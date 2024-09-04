from .config import Config
from .logger import logger
from .exceptions import AIConsensusError, ModelQueryError, VotingError, DatabaseError
import anthropic
from .base_model import BaseModel

class AnthropicModel(BaseModel):
    def __init__(self):
        self.client = anthropic.Anthropic(api_key="your-anthropic-api-key")  # Set this securely
        self._name = "Anthropic"

    @property
    def name(self):
        return self._name

    def query(self, formatted_query, max_tokens, temperature):
        response = self.client.completions.create(
            model="claude-2",
            prompt=f"\n\nHuman: {formatted_query}\n\nAssistant:",
            max_tokens_to_sample=max_tokens,
            temperature=temperature
        )
        return response.completion

    def vote_on_responses(self, responses):
        voting_prompt = "Rate each of the following responses on a scale of 1 to 10, where 10 is the best:\n\n"
        for model, response in responses.items():
            voting_prompt += f"{model}: {response}\n\n"
        voting_prompt += "Provide your ratings as a JSON object with model names as keys and ratings as values."

        vote_response = self.client.completions.create(
            model="claude-2",
            prompt=f"\n\nHuman: {voting_prompt}\n\nAssistant:",
            max_tokens_to_sample=1000,
            temperature=0.2
        )
        
        # Parse the JSON response
        import json
        return json.loads(vote_response.completion)