# Sentiment Analysis API

A REST API built with Python, FastAPI, and Hugging Face Transformers that classifies text as **positive, negative, or neutral** and returns confidence scores for each sentiment class.

## Features

- Positive, negative, and neutral sentiment classification
- Confidence score for the predicted sentiment
- Per-class probability scores
- Single-text sentiment analysis
- Batch sentiment analysis for up to 10 texts
- Input validation
- Error handling
- Automatic API documentation with Swagger UI
- Automated tests using Pytest

## Tech Stack

- Python 3.12
- FastAPI
- Hugging Face Transformers
- PyTorch
- Pydantic
- Pytest
- Uvicorn

## Model

This project uses the pretrained:

`cardiffnlp/twitter-roberta-base-sentiment-latest`

The model is based on RoBERTa and supports three sentiment classes:

- Positive
- Neutral
- Negative

No custom model training is required.

## Project Structure

```text
sentiment-analysis-api/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── model.py
│   ├── routes.py
│   └── schemas.py
│
├── tests/
│   └── test_api.py
│
├── .gitignore
├── pytest.ini
├── requirements.txt
└── README.md