#LLM Translation API

A simple FastAPI-based LLM inference service using LangChain, LangServe, and Groq to translate text into different languages.

#Features

FastAPI backend

LangChain prompt pipeline

Groq LLM integration

LangServe API endpoint

#Setup
pip install -r requirements.txt


Create a .env file:

GROQ_API_KEY=your_groq_api_key

#Run
python serve.py


#Server runs at:

http://127.0.0.1:8000

#API

POST /chain

{
  "input": {
    "language": "Spanish",
    "text": "Hello world"
  }
}

#Docs

Swagger UI: /docs
