from pydantic import BaseModel, Field, field_validator


class TextRequest(BaseModel):
    text: str = Field(
        ...,
        min_length=1,
        max_length=5000,
        description="Text to analyze for sentiment"
    )

    @field_validator("text")
    @classmethod
    def validate_text(cls, value: str):
        if not value.strip():
            raise ValueError("Text cannot be empty or contain only spaces")
        return value


class SentimentResponse(BaseModel):
    sentiment: str
    confidence: float
    scores: dict[str, float]


class BatchRequest(BaseModel):
    texts: list[str] = Field(
        ...,
        min_length=1,
        max_length=10,
        description="List containing 1 to 10 texts"
    )

    @field_validator("texts")
    @classmethod
    def validate_texts(cls, values: list[str]):
        for text in values:
            if not text.strip():
                raise ValueError("Texts cannot be empty or contain only spaces")
            if len(text) > 5000:
                raise ValueError("Each text must be 5000 characters or less")

        return values


class BatchResponse(BaseModel):
    results: list[SentimentResponse]