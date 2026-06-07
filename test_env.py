import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
print(f"API Key loaded: {api_key}")
print(f"Key length: {len(api_key) if api_key else 0}")
print(f"Starts with AQ: {api_key.startswith('AQ.') if api_key else False}")
