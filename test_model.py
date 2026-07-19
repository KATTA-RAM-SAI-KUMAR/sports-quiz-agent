import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

models = [
    "gemini-2.0-flash",
    "gemini-2.0-flash-lite",
    "gemini-2.5-flash-lite",
    "gemini-flash-latest",
    "gemini-3.5-flash"
]

for model in models:
    try:
        response = client.models.generate_content(
            model=model,
            contents="Say Hello"
        )
        print(f"✅ {model} works")
        print(response.text)
        break
    except Exception as e:
        print(f"❌ {model} failed")
        print(e)
        print("-" * 50)