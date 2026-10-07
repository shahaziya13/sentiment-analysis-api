from sklearn.metrics import accuracy_score, precision_recall_fscore_support
from app.model import analyze_sentiment


# Small labeled evaluation dataset
test_data = [
    ("I absolutely loved this movie!", "positive"),
    ("This was an amazing experience.", "positive"),
    ("I really enjoyed the product.", "positive"),
    ("The service was excellent.", "positive"),
    ("This is fantastic and works perfectly.", "positive"),
    ("I am very happy with the results.", "positive"),
    ("What a wonderful experience!", "positive"),
    ("The movie was brilliant.", "positive"),
    ("I hate this movie.", "negative"),
    ("This was the worst experience ever.", "negative"),
    ("The product is terrible.", "negative"),
    ("I am extremely disappointed.", "negative"),
    ("The service was awful.", "negative"),
    ("This completely failed.", "negative"),
    ("I regret buying this.", "negative"),
    ("The experience was horrible.", "negative"),
    ("The movie was released yesterday.", "neutral"),
    ("The package arrived this morning.", "neutral"),
    ("The meeting starts at 10 AM.", "neutral"),
    ("The product costs 50 dollars.", "neutral"),
    ("The company announced a new update.", "neutral"),
    ("The train arrived at the station.", "neutral"),
    ("The event is scheduled for Friday.", "neutral"),
    ("The application was updated today.", "neutral"),
]


texts = [item[0] for item in test_data]
true_labels = [item[1] for item in test_data]


print("Running model predictions...")


predicted_labels = []

for text in texts:
    result = analyze_sentiment(text)
    predicted_labels.append(result["sentiment"])


accuracy = accuracy_score(true_labels, predicted_labels)

precision, recall, f1, _ = precision_recall_fscore_support(
    true_labels,
    predicted_labels,
    labels=["negative", "neutral", "positive"],
    average="weighted",
    zero_division=0
)


print("\n===== MODEL METRICS =====")
print(f"Test samples: {len(test_data)}")
print(f"Accuracy    : {accuracy:.4f}")
print(f"Precision   : {precision:.4f}")
print(f"Recall      : {recall:.4f}")
print(f"F1 Score    : {f1:.4f}")