from openai import OpenAI
from config import Config


def load_client():
    client = OpenAI(
        api_key=Config.API_KEY,
        base_url=Config.API_URL
    )
    return client