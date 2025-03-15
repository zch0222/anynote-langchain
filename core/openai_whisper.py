from openai import OpenAI
from core.config import OPENAI_WHISPER_API_KEY, OPENAI_WHISPER_BASE_URL

def get_openai_whisper_client():
    client = OpenAI(api_key=OPENAI_WHISPER_API_KEY, base_url=OPENAI_WHISPER_BASE_URL)
    return client