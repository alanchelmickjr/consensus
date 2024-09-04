import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from eracai.main import consensus_response
from eracai.chat_message import ChatMessage

@pytest.mark.asyncio
async def test_consensus_response():
    query = "Who is the hottest actress today?"
    result = await consensus_response(query)
    
    assert isinstance(result, ChatMessage)
    assert result.role == "assistant"
    assert len(result.content) > 0
    assert "Paris" in result.content.lower()
    assert "voting_results" in result.metadata
    assert "participating_models" in result.metadata

@pytest.mark.asyncio
async def test_consensus_response_error():
    with pytest.raises(Exception):
        await consensus_response(None)