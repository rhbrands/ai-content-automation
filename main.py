import os
from dotenv import load_dotenv
from scripts.script_generator import generate_script
from scripts.text_to_speech import generate_audio
from scripts.video_creator import create_video
from utils.logger import setup_logger

# Load environment variables
load_dotenv()

logger = setup_logger(__name__)

def run_daily_automation(topic):
    """Main workflow: Idea → Script → Voice → Video"""
    
    try:
        logger.info("=" * 60)
        logger.info(f"🚀 Starting automation for topic: {topic}")
        logger.info("=" * 60)
        
        # Step 1: Generate script
        logger.info("📝 Step 1: Generating script...")
        script = generate_script(topic)
        logger.info(f"Generated Script:\n{script}\n")
        
        # Step 2: Generate audio
        logger.info("🎙️ Step 2: Generating audio...")
        audio_file = generate_audio(script, output_file="temp_audio.mp3")
        
        if audio_file and os.path.exists(audio_file):
            logger.info(f"Audio file: {audio_file}")
            
            # Step 3: Create video
            logger.info("🎬 Step 3: Creating video...")
            video_file = create_video(audio_file, output_file="temp_video.mp4")
            logger.info(f"Video file: {video_file}")
        else:
            logger.info("Skipping video creation (no audio file)")
            video_file = None
        
        logger.info("=" * 60)
        logger.info("✅ Automation complete!")
        logger.info("=" * 60)
        
        return {
            "script": script,
            "audio": audio_file,
            "video": video_file,
            "status": "success"
        }
        
    except Exception as e:
        logger.error(f"❌ Automation failed: {str(e)}", exc_info=True)
        return {
            "status": "error",
            "error": str(e)
        }

if __name__ == "__main__":
    result = run_daily_automation("AI automation tips for content creators")
    print(f"Result: {result['status']}")
