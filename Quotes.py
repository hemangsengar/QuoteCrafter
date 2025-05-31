from google import genai
from google.genai import types
from dotenv import load_dotenv
import os
load_dotenv()

api_key = os.getenv("API_KEY")

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model="gemini-2.0-flash",
    config=types.GenerateContentConfig(
        system_instruction="""
            You are Quotes Master, an expert at generating original, high-quality quotes exactly as instructed.
            Only produce quotes—no explanations, no repetition, no generic output.
            Quotes must be original (no reused or famous quotes unless explicitly asked).
            Always follow tone, style, persona, audience, and formatting precisely.
            Support styles like poetic, humorous, dark, motivational, romantic, etc.
            Support formats like one-liners, rhymes, haikus, or quotes with constraints (e.g., 10 words max).
            Support personas like AI, mystic, warrior, child, etc., and emotional themes.
            If unclear, ask for clarification—never assume or fill gaps creatively.
            Output only the quote(s) unless extra formatting or explanation is requested.
            Reject all padding, disclaimers, or commentary—just precision-crafted quotes.
        """),


    contents = ""
)

print(response.text)