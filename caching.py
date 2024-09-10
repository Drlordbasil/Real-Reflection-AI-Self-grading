import json
from datetime import datetime, timedelta
import os
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Cache:
    def __init__(self, cache_dir='cache'):
        self.cache_dir = cache_dir
        if not os.path.exists(cache_dir):
            os.makedirs(cache_dir)

    def get(self, key):
        file_path = os.path.join(self.cache_dir, f"{key}.json")
        if os.path.exists(file_path):
            try:
                with open(file_path, 'r') as f:
                    data = json.load(f)
                    if 'expiry' in data and 'value' in data:
                        if datetime.now() < datetime.fromisoformat(data['expiry']):
                            return data['value']
                        else:
                            logging.info(f"Cache expired for key: {key}")
                    else:
                        logging.warning(f"Invalid cache structure for key: {key}")
            except json.JSONDecodeError:
                logging.error(f"Error decoding JSON for key: {key}")
            except Exception as e:
                logging.error(f"Error reading cache for key: {key}. Error: {str(e)}")
        return None

    def set(self, key, value, expiry_hours=24):
        file_path = os.path.join(self.cache_dir, f"{key}.json")
        expiry = datetime.now() + timedelta(hours=expiry_hours)
        data = {
            'value': value,
            'expiry': expiry.isoformat()
        }
        try:
            with open(file_path, 'w') as f:
                json.dump(data, f)
            logging.info(f"Cache set for key: {key}")
        except Exception as e:
            logging.error(f"Error setting cache for key: {key}. Error: {str(e)}")

cache = Cache()