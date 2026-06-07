# AI Content Automation

AI Content Automation is a modular Python workflow for generating social media-ready video content from a topic prompt.

The pipeline includes:
- script generation via Google Gemini free tier
- fallback Hugging Face generation when Gemini is unavailable
- text-to-speech audio rendering
- image-based video creation with placeholder support

## Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/ai-content-automation.git
cd ai-content-automation
```

### 2. Create and activate the virtual environment
```bash
python -m venv venv
# macOS / Linux
source venv/bin/activate
# Windows PowerShell
venv\Scripts\Activate.ps1
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure environment variables
Copy the example environment file and update the values:
```bash
copy .env.example .env
```

Edit `.env` and provide:
- `GEMINI_API_KEY` for Google Gemini free tier
- `HUGGINGFACE_API_KEY` for Hugging Face fallback (optional)
- `GOOGLE_TTS_CREDENTIALS` for Google Cloud Text-to-Speech
- `YOUTUBE_CREDENTIALS` and `YOUTUBE_CHANNEL_ID` if uploading videos

### 5. Add stock images (optional)
Add image assets to `assets/stock_images/` for video generation. If no images are available, the project will generate a placeholder video.

### 6. Run the automation
```bash
python main.py
```

## Project Structure
```text
ai-content-automation/
├── assets/              # Static assets and stock images
├── scripts/             # Core workflow modules
│   ├── script_generator.py
│   ├── text_to_speech.py
│   └── video_creator.py
├── utils/               # Utility modules
│   └── logger.py
├── config.py            # Project configuration and paths
├── main.py              # Main orchestration script
├── requirements.txt     # Python dependencies
├── .env.example         # Environment variable template
└── README.md            # Project documentation
```

## Features
- free-tier Gemini script generation
- Hugging Face fallback for resilience
- Google Cloud Text-to-Speech audio creation
- automated video assembly from image assets or placeholder backgrounds
- structured logging and modular architecture

## Notes
- YouTube upload integration is not active by default.
- Make sure API keys are valid and `GOOGLE_TTS_CREDENTIALS` points to a valid JSON key file.

## License
MIT
