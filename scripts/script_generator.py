import os
import requests
from config import GEMINI_API_KEY
from utils.logger import setup_logger

logger = setup_logger(__name__)

def fallback_script(topic):
    return (
        f"Hook: Here's a quick tip on {topic}. [PAUSE]\n"
        f"Body: This is valuable content about {topic}. [PAUSE]\n"
        "CTA: Try this yourself and subscribe for more tips."
    )


def generate_huggingface_script(topic, length=60):
    hf_token = os.getenv("HUGGINGFACE_API_KEY")
    if not hf_token:
        return None

    url = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1"
    headers = {
        "Authorization": f"Bearer {hf_token}",
        "Content-Type": "application/json"
    }
    prompt = f"""Create a {length}-second social media script about: {topic}

Format:
- Hook (5s): Grab attention immediately
- Body ({length-20}s): Main content and value
- CTA (15s): Call to action

Requirements:
- Punchy and engaging
- Natural speaking style
- Include [PAUSE] for emphasis
- Make it shareable and viral-worthy

Output ONLY the script text, no other commentary."""

    try:
        response = requests.post(
            url,
            headers=headers,
            json={"inputs": prompt, "options": {"wait_for_model": True}},
            timeout=30
        )

        if response.status_code == 200:
            result = response.json()
            if isinstance(result, list) and result:
                return result[0].get("generated_text") or fallback_script(topic)
            if isinstance(result, dict) and result.get("generated_text"):
                return result["generated_text"]

        logger.warning(f"Hugging Face API failed: {response.status_code} - {response.text}")
        return None

    except Exception as e:
        logger.warning(f"Hugging Face script generation failed: {str(e)}")
        return None


def generate_script(topic, length=60):
    """Generate script using free tier providers."""

    if GEMINI_API_KEY:
        logger.info("ℹ️ Attempting Gemini free tier for script generation.")
        url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent"

        prompt = f"""Create a {length}-second social media script about: {topic}

Format:
- Hook (5s): Grab attention immediately
- Body ({length-20}s): Main content and value
- CTA (15s): Call to action

Requirements:
- Punchy and engaging
- Natural speaking style
- Include [PAUSE] for emphasis
- Make it shareable and viral-worthy

Output ONLY the script text, no other commentary."""

        payload = {
            "contents": [{
                "parts": [{
                    "text": prompt
                }]
            }]
        }

        headers = {"Content-Type": "application/json"}

        try:
            response = requests.post(
                f"{url}?key={GEMINI_API_KEY}",
                json=payload,
                headers=headers,
                timeout=30
            )

            if response.status_code == 200:
                result = response.json()
                script = result['candidates'][0]['content']['parts'][0]['text']
                logger.info("✅ Gemini script generated")
                return script

            logger.warning(f"Gemini API failed: {response.status_code} - {response.text}")
        except Exception as e:
            logger.warning(f"Gemini script generation failed: {str(e)}")

    hf_script = generate_huggingface_script(topic, length=length)
    if hf_script:
        logger.info("✅ Hugging Face script generated")
        return hf_script

    if not GEMINI_API_KEY:
        logger.warning("No Gemini key configured.")
        logger.info("Using local fallback script because Gemini is unavailable.")
    else:
        logger.warning("Falling back from Gemini to Hugging Face or local script.")
        logger.info("Using local fallback script.")

    return fallback_script(topic)


if __name__ == "__main__":
    print(generate_script("AI automation tips"))
