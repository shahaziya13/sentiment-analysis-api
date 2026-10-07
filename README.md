# Sentiment Analysis API

A REST API for classifying text as **positive, negative, or neutral** using a pretrained Hugging Face sentiment analysis model.

Built with **Python, FastAPI, Hugging Face Transformers, and PyTorch**.

## Features

- Positive, negative, and neutral sentiment classification
- Confidence score for each prediction
- Per-class sentiment scores
- Single-text sentiment analysis
- Batch sentiment analysis
- Batch requests limited to 10 texts
- Input validation
- Error handling
- Health check endpoint
- Interactive Swagger API documentation
- Automated API tests
- Model evaluation metrics

## Tech Stack

- Python
- FastAPI
- Hugging Face Transformers
- PyTorch
- Pydantic
- Scikit-learn
- Pytest
- Uvicorn

## Model

The API uses the pretrained:

`cardiffnlp/twitter-roberta-base-sentiment-latest`

The model supports three sentiment classes:

- Positive
- Neutral
- Negative

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
├── evaluate.py
├── metrics.md
├── .gitignore
├── pytest.ini
├── requirements.txt
└── README.md