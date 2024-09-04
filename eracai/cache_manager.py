class CacheManager:
    def __init__(self):
        self.cache = {}
    
    def get(self, model_name, query):
        return self.cache.get((model_name, query))
    
    def set(self, model_name, query, response):
        self.cache[(model_name, query)] = response