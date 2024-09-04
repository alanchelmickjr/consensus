import weaviate
import os
from datetime import datetime

class DBManager:
    def __init__(self):
        # Set these environment variables
        URL = "YOUR_WEAVIATE_URL.gcp.weaviate.cloud"
        APIKEY = "YOUR_API_KEY"
        
        # Connect to a WCS instance
        self.client = weaviate.Client(
            url=URL,
            auth_client_secret=weaviate.AuthApiKey(api_key=APIKEY)
        )

        self.ensure_schema()
        
    def ensure_schema(self):
        class_name = "AIConsensusResponse"
        if not self.client.schema.exists(class_name):
            schema = {
                "class": class_name,
                "properties": [
                    {"name": "query", "dataType": ["text"]},
                    {"name": "response", "dataType": ["text"]},
                    {"name": "timestamp", "dataType": ["date"]}
                ]
            }
            self.client.schema.create_class(schema)
        else:
            print(f"Schema for {class_name} already exists.")

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
