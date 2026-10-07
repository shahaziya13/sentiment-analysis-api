from fastapi import APIRouter, HTTPException

from app.model import analyze_sentiment
from app.schemas import (
    TextRequest,
    SentimentResponse,
    BatchRequest,
    BatchResponse,
)

router = APIRouter(prefix="/api", tags=["Sentiment Analysis"])


@router.post("/analyze", response_model=SentimentResponse)
def analyze_text(request: TextRequest):
    try:
        return analyze_sentiment(request.text)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Sentiment analysis failed: {str(e)}"
        )


@router.post("/analyze/batch", response_model=BatchResponse)
def analyze_batch(request: BatchRequest):
    try:
        results = [
            analyze_sentiment(text)
            for text in request.texts
        ]

        return {"results": results}

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Batch sentiment analysis failed: {str(e)}"
        )