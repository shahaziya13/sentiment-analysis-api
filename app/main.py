from fastapi import FastAPI

from app.routes import router


app = FastAPI(
    title="Sentiment Analysis API",
    description="An API for classifying text as positive, negative, or neutral.",
    version="1.0.0",
)


app.include_router(router)


@app.get("/")
def root():
    return {
        "message": "Sentiment Analysis API is running",
        "docs": "/docs"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }