import os
import json

from dotenv import load_dotenv
from google import genai

from src.database import search_data
from src.search import search_web

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))


def generate_quiz(sport):
    # Get data from ChromaDB
    database_results = search_data(sport)

    # Get latest news from web
    web_results = search_web(f"Latest {sport} news")

    # Convert lists into strings
    context = "\n".join(database_results)
    latest_news = "\n".join(web_results)

    # Prompt for Gemini
    prompt = f"""
You are an expert sports quiz generator.

Use the following information to create a quiz.

Sports Facts:
{context}

Latest News:
{latest_news}

Generate exactly 5 multiple-choice questions.

Return ONLY valid JSON.

Example format:

[
  {{
    "question": "Which country won the ICC Men's T20 World Cup in 2024?",
    "options": [
      "Australia",
      "England",
      "India",
      "South Africa"
    ],
    "answer": "India",
    "difficulty": "Easy"
  }},
  {{
    "question": "Another question",
    "options": [
      "Option A",
      "Option B",
      "Option C",
      "Option D"
    ],
    "answer": "Option B",
    "difficulty": "Medium"
  }}
]

Rules:
1. Generate exactly 5 questions.
2. Each question must have exactly 4 options.
3. Only one option should be correct.
4. Difficulty should be Easy, Medium, or Hard.
5. Do NOT return markdown.
6. Do NOT use ```json.
7. Do NOT write explanations.
8. Return ONLY the JSON array.
"""

    # Generate quiz
    response = client.models.generate_content(
        model="gemini-flash-latest",
        contents=prompt
    )

    text = response.text.strip()

    # Remove markdown if Gemini returns it
    if text.startswith("```json"):
        text = text.replace("```json", "").replace("```", "").strip()

    elif text.startswith("```"):
        text = text.replace("```", "").strip()

    # Convert JSON string to Python list
    quiz = json.loads(text)

    return quiz