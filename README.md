# AI Content Automation System

Automated workflow: Idea → Script → AI Voice → Video → Upload

## Setup Instructions

### 1. Clone the repository
\`\`\`bash
git clone https://github.com/YOUR_USERNAME/ai-content-automation.git
cd ai-content-automation
\`\`\`

### 2. Create virtual environment
\`\`\`bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
\`\`\`

### 3. Install dependencies
\`\`\`bash
pip install -r requirements.txt
\`\`\`

### 4. Set up API keys
Copy `.env.example` to `.env`:
\`\`\`bash
cp .env.example .env
\`\`\`

Then fill in your API keys:
- **Gemini API**: Get from [Google AI Studio](https://aistudio.google.com/app/apikey)
- **YouTube API**: Set up from [Google Cloud Console](https://console.cloud.google.com)

### 5. Add stock images
Place images in `assets/stock_images/` for video generation.

### 6. Run the automation
\`\`\`bash
python main.py
\`\`\`

## Project Structure
\`\`\`
ai-content-automation/
├── scripts/              # Core automation modules
│   ├── script_generator.py
│   ├── text_to_speech.py
│   └── video_creator.py
├── utils/               # Utilities
│   └── logger.py
├── assets/              # Static files
│   └── stock_images/
├── main.py              # Main workflow
├── config.py            # Configuration
├── requirements.txt     # Dependencies
└── .env.example         # API key template
\`\`\`

## Features
- ✅ AI script generation (Google Gemini)
- ✅ Text-to-speech conversion (pyttsx3)
- ✅ Video creation with images
- ✅ Logging system
- ✅ Modular architecture

## Next Steps
- [ ] YouTube API integration
- [ ] Instagram/Facebook automation
- [ ] Scheduled daily runs
- [ ] Make.com/n8n integration

## License
MIT
