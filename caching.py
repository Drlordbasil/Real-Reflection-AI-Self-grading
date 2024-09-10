import json
import os
from datetime import datetime, timedelta

class Cache:
    def __init__(self, cache_dir='cache', expiration_time=3600):  # 1 hour expiration by default
        self.cache_dir = cache_dir
        self.expiration_time = expiration_time
        os.makedirs(cache_dir, exist_ok=True)

    def _get_cache_file_path(self, key):
        return os.path.join(self.cache_dir, f"{key}.json")

    def get(self, key):
        file_path = self._get_cache_file_path(key)
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                data = json.load(f)
            if datetime.now().timestamp() - data['timestamp'] < self.expiration_time:
                return data['value']
        return None

    def set(self, key, value):
        file_path = self._get_cache_file_path(key)
        with open(file_path, 'w') as f:
            json.dump({
                'timestamp': datetime.now().timestamp(),
                'value': value
            }, f)

cache = Cache()