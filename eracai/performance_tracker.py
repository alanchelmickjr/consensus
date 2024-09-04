from .db_manager import DBManager

class PerformanceTracker:
    def __init__(self):
        self.db = DBManager()

    async def track_performance(self, model_name, query, response, selected):
        await self.db.store_performance(model_name, query, response, selected)

    async def get_model_performance(self, model_name):
        return await self.db.get_model_performance(model_name)