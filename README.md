# 🏆 AI-Powered Sports Quiz Generation Agent

An AI-powered Sports Quiz Generator built using Retrieval-Augmented Generation (RAG), Google Gemini, ChromaDB, DuckDuckGo Search, and Streamlit.

## Features

- Generate quizzes for multiple sports
- Choose difficulty level (Easy, Medium, Hard)
- Uses RAG for accurate question generation
- Retrieves sports knowledge from ChromaDB
- Fetches recent sports information using DuckDuckGo Search
- Generates quizzes using Google Gemini
- Interactive Streamlit interface
- Displays score and correct answers after submission

## Tech Stack

- Python
- Streamlit
- Google Gemini API
- ChromaDB
- LangChain
- DDGS (DuckDuckGo Search)

## Project Structure

```
sports-quiz-agent/
│
├── app.py
├── requirements.txt
├── README.md
├── data/
│   └── sports_facts.json
├── src/
│   ├── database.py
│   ├── search.py
│   └── generator.py
└── .env
```

## Installation

Clone the repository:

```bash
git clone https://github.com/KATTA-RAM-SAI-KUMAR/sports-quiz-agent.git
cd sports-quiz-agent
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

Run the application:

```bash
streamlit run app.py
```

## How It Works

1. User selects a sport and difficulty.
2. Relevant sports facts are retrieved from ChromaDB.
3. Latest sports information is fetched using DuckDuckGo Search.
4. Google Gemini generates quiz questions using retrieved context.
5. User answers the quiz and receives a final score.

## Future Improvements

- User authentication
- Leaderboard
- Timer-based quizzes
- Quiz history
- More sports categories

## Author

**K Ram Sai Kumar**