from .config import Config
from .logger import logger
from .exceptions import AIConsensusError, ModelQueryError, VotingError, DatabaseError
import groq
from .base_model import BaseModel

class GroqModel(BaseModel):
    def __init__(self):
        self.client = groq.Groq(api_key="your-groq-api-key")  # Set this securely
        self._name = "Groq"

    @property
    def name(self):
        return self._name

    def query(self, formatted_query, max_tokens, temperature):
        response = self.client.chat.completions.create(
            model="mixtralx7b-",
            messages=[{"role": "user", "content": formatted_query}],
            max_tokens=max_tokens,
            temperature=temperature
        )
        return response.choices[0].message.content

    def vote_on_responses(self, responses):
        voting_prompt = "Rate each of the following responses on a scale of 1 to 10, where 10 is the best:\n\n"
        for model, response in responses.items():
            voting_prompt += f"{model}: {response}\n\n"
        voting_prompt += "Provide your ratings as a JSON object with model names as keys and ratings as values."

        vote_response = self.client.chat.completions.create(
            model="mixtral-8x7b-32768",
            messages=[{"role": "user", "content": voting_prompt}],
            max_tokens=1000,
            temperature=0.2
        )
        
        # Parse the JSON response
        import json
        return json.loads(vote_response.choices[0].message.content)