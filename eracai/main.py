import asyncio
from .models.config import Config
from .models.logger import logger
from .models.exceptions import AIConsensusError, ModelQueryError, VotingError, DatabaseError
from .models import get_all_models as get_all_models_func
from .query_formatter import format_query
from .db_manager import DBManager
from collections import Counter
from .chat_message import ChatMessage

async def async_query_model(model, formatted_query, max_tokens, temperature):
    try:
        return await model.async_query(formatted_query, max_tokens, temperature)
    except Exception as e:
        logger.error(f"Error querying {model.name}: {str(e)}")
        return None

async def consensus_response(query, max_tokens=1000, temperature=0.7) -> ChatMessage:
    try:
        db = DBManager()

        formatted_query = format_query(query)

        models = get_all_models_func()
        tasks = [async_query_model(model, formatted_query, max_tokens, temperature) for model in models]

        responses = await asyncio.gather(*tasks)
        responses = {model.name: response for model, response in zip(models, responses) if response is not None}

        if not responses:
            raise AIConsensusError("No valid responses received from any model")

        # Majority voting
        votes = Counter(responses.values())
        consensus = votes.most_common(1)[0][0]

        voting_results = {model_name: (1 if response == consensus else 0) for model_name, response in responses.items()}

        result = {
            "query": query,
            "response": consensus,
            "voting_results": voting_results,
            "participating_models": list(responses.keys())
        }

        # Store in Weaviate
        await db.store_response(result)

        # Create and return a ChatMessage
        return ChatMessage(
            role="assistant",
            content=consensus,
            metadata={
                "voting_results": voting_results,
                "participating_models": list(responses.keys())
            }
        )
    except Exception as e:
        raise AIConsensusError(f"Error in consensus response: {str(e)}")