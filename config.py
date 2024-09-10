import os

class Config:
    API_KEY = os.getenv("GROQ_API_KEY")
    API_URL = "https://api.groq.com/openai/v1"
    RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")  # Add this line
    text_gen_funct_call_model = "llama-3.1-70b-versatile"
    regular_model = "llama-3.1-70b-versatile"
    image_vision_model = "llava-v1.5-7b-4096-preview"
    whisper_model = "distil-whisper-large-v3-en"
