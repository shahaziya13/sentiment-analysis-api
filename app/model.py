from transformers import pipeline


# Load the pretrained sentiment analysis model
sentiment_pipeline = pipeline(
    "sentiment-analysis",
    model="cardiffnlp/twitter-roberta-base-sentiment-latest",
    top_k=None
)


def analyze_sentiment(text: str):
    results = sentiment_pipeline(text)

    # Handle the pipeline output format
    if results and isinstance(results[0], list):
        results = results[0]

    scores = {}

    for result in results:
        label = result["label"].lower()
        score = result["score"]

        scores[label] = round(score, 4)

    sentiment = max(scores, key=scores.get)
    confidence = scores[sentiment]

    return {
        "sentiment": sentiment,
        "confidence": confidence,
        "scores": scores
    }