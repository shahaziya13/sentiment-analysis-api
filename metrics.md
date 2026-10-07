# Model Evaluation

## Model

- Model: `cardiffnlp/twitter-roberta-base-sentiment-latest`
- Task: 3-class sentiment classification
- Classes: Negative, Neutral, Positive

## Evaluation Dataset

A manually labeled evaluation set containing 24 representative text samples was used to evaluate the API's sentiment classification performance.

The evaluation set contains:

- 8 positive samples
- 8 negative samples
- 8 neutral samples

## Results

| Metric | Score |
|---|---:|
| Accuracy | 95.83% |
| Precision | 96.30% |
| Recall | 95.83% |
| F1 Score | 95.82% |

## Notes

The reported metrics are based on the project's 24-sample evaluation set. These results demonstrate the model's performance on the selected test examples but should not be interpreted as a general benchmark for the pretrained model.

The model was selected because it supports three sentiment classes: positive, negative, and neutral.