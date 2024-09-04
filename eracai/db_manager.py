from .config import Config
from .logger import logger
from .exceptions import AIConsensusError, ModelQueryError, VotingError, DatabaseError
import weaviate
from datetime import datetime

class DBManager:
    def __init__(self):
        self.client = weaviate.Client("http://localhost:8080")  # Adjust URL as needed
        self.ensure_schema()

    def ensure_schema(self):
        # Create schema if it doesn't exist
        schema = {
            "class": "AIConsensusResponse",
            "properties": [
                {"name": "query", "dataType": ["text"]},
                {"name": "response", "dataType": ["text"]},
                {"name": "timestamp", "dataType": ["date"]}
            ]
        }
        self.client.schema.create_class(schema)

    def store_best_response(self, query, response):
        # Store in Weaviate
        self.client.data_object.create(
            "AIConsensusResponse",
            {
                "query": query,
                "response": response,
                "timestamp": datetime.now().isoformat()
            }
        )

    def add_to_fine_tuning_dataset(self, query, response):
        # Append to a file in chat format for fine-tuning
        with open("fine_tuning_dataset.jsonl", "a") as f:
            f.write(f'{{"messages": [{{"role": "user", "content": "{query}"}}, {{"role": "assistant", "content": "{response}"}}]}}\n')
