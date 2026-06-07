import pyttsx3
import os
from utils.logger import setup_logger

logger = setup_logger(__name__)

def generate_audio(text, output_file="temp_audio.mp3", rate=150):
    """Convert text to speech using pyttsx3 (free, offline, no API needed)"""
    
    try:
        engine = pyttsx3.init()
        engine.setProperty('rate', rate)  # Speed of speech
        engine.setProperty('volume', 0.9)  # Volume level
        
        # Save to file
        engine.save_to_file(text, output_file)
        engine.runAndWait()
        
        logger.info(f"✅ Audio generated: {output_file}")
        return output_file
        
    except Exception as e:
        logger.error(f"❌ Error generating audio: {str(e)}")
        return None

if __name__ == "__main__":
    sample_text = "Hello! This is a test of the text to speech system."
    generate_audio(sample_text)
