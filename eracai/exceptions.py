class AIConsensusError(Exception):
    pass

class ModelQueryError(AIConsensusError):
    pass

class VotingError(AIConsensusError):
    pass

class DatabaseError(AIConsensusError):
    pass