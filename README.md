# LLM Translation API
Overview

A lightweight FastAPI-based LLM service that uses LangChain, LangServe, and Groq to translate text into different languages via a REST API.

# Features

FastAPI backend

LangChain prompt templates

Groq LLM integration

LangServe API endpoint

Technologies Used

Python

FastAPI

LangChain

LangServe

Groq

# Installation
1. Install Dependencies
pip install -r requirements.txt

2. Environment Setup

Create a .env file:

GROQ_API_KEY=your_groq_api_key

# Running the Application
python serve.py


# Server runs at:

http://127.0.0.1:8000

# API Usage
Endpoint

POST /chain

Request Example
{
  "input": {
    "language": "French",
    "text": "Hello"
  }
}

# API Documentation

Swagger UI: http://127.0.0.1:8000/docs
