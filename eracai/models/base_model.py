from .config import Config
from .logger import logger
from .exceptions import AIConsensusError, ModelQueryError, VotingError, DatabaseError
from abc import ABC, abstractmethod

class BaseModel(ABC):
    @abstractmethod
    def query(self, formatted_query, max_tokens, temperature):
        pass
    
    @abstractmethod
    def vote_on_responses(self, responses):
        pass

    @property
    @abstractmethod
    def name(self):
        pass