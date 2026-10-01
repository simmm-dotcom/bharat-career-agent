import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

key = os.getenv("GEMINI_API_KEY")

print("API key loaded:", bool(key))

client = genai.Client(api_key=key)

response = client.models.generate_content(
    model=os.getenv("GEMINI_MODEL", "gemini-2.5-flash"),
    contents="Reply with exactly: Gemini is working"
)

print(response.text)