from PIL import Image
if not hasattr(Image, "ANTIALIAS"):
    if hasattr(Image, "Resampling"):
        Image.ANTIALIAS = Image.Resampling.LANCZOS
    else:
        Image.ANTIALIAS = Image.LANCZOS

from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips, ColorClip
import os
from config import STOCK_IMAGES_DIR
from utils.logger import setup_logger

logger = setup_logger(__name__)

def create_video(audio_file, output_file="temp_video.mp4", image_dir=None):
    """Create video by combining images and audio"""
    
    if image_dir is None:
        image_dir = STOCK_IMAGES_DIR
    
    # Get all images
    images = [
        os.path.join(image_dir, img)
        for img in os.listdir(image_dir)
        if img.lower().endswith((".jpg", ".png", ".jpeg"))
    ]
    
    if not images:
        logger.warning(f"No images found in {image_dir}. Creating placeholder...")
        return create_video_with_placeholder(audio_file, output_file)
    
    try:
        audio = AudioFileClip(audio_file)
        duration = audio.duration
        
        logger.info(f"Creating video with {len(images)} images, duration: {duration:.2f}s")
        
        # Create clips from images
        clips = []
        img_duration = duration / len(images)
        
        for i, img in enumerate(images):
            try:
                clip = ImageClip(img).set_duration(img_duration).resize(height=1080)
                clips.append(clip)
            except Exception as e:
                logger.warning(f"Could not load image {img}: {str(e)}")
        
        if not clips:
            logger.error("No valid images could be loaded")
            return create_video_with_placeholder(audio_file, output_file)
        
        video = concatenate_videoclips(clips)
        video = video.set_audio(audio)
        
        logger.info(f"Writing video to {output_file}...")
        video.write_videofile(output_file, fps=24, verbose=False, logger=None)
        
        logger.info(f"✅ Video created: {output_file}")
        return output_file
        
    except Exception as e:
        logger.error(f"❌ Error creating video: {str(e)}")
        raise

def create_video_with_placeholder(audio_file, output_file="temp_video.mp4"):
    """Create video with a solid color placeholder"""
    
    try:
        audio = AudioFileClip(audio_file)
        duration = audio.duration
        
        # Create a black background
        placeholder = ColorClip(size=(1920, 1080), color=(0, 0, 0)).set_duration(duration)
        placeholder = placeholder.set_audio(audio)
        
        logger.info(f"Creating placeholder video...")
        placeholder.write_videofile(output_file, fps=24, verbose=False, logger=None)
        
        logger.info(f"✅ Placeholder video created: {output_file}")
        return output_file
        
    except Exception as e:
        logger.error(f"❌ Error creating placeholder: {str(e)}")
        raise

if __name__ == "__main__":
    if os.path.exists("temp_audio.mp3"):
        create_video("temp_audio.mp3")
    else:
        logger.info("No audio file found. Run text_to_speech.py first.")
