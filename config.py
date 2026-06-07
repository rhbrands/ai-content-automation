import os
from dotenv import load_dotenv

load_dotenv()

# API Keys
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GOOGLE_TTS_CREDENTIALS = os.getenv("GOOGLE_TTS_CREDENTIALS")
YOUTUBE_CREDENTIALS = os.getenv("YOUTUBE_CREDENTIALS")
YOUTUBE_CHANNEL_ID = os.getenv("YOUTUBE_CHANNEL_ID")

# Paths
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(PROJECT_ROOT, "assets")
STOCK_IMAGES_DIR = os.path.join(ASSETS_DIR, "stock_images")
LOGS_DIR = os.path.join(PROJECT_ROOT, "logs")

# Ensure directories exist
os.makedirs(LOGS_DIR, exist_ok=True)
os.makedirs(STOCK_IMAGES_DIR, exist_ok=True)
