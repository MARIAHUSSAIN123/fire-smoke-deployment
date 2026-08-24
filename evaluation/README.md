# Model Evaluation

This folder contains the evaluation results of the Fire / Smoke Detection model.

## Dataset Distribution

The dataset was divided into training, validation, and testing sets.

### Training Set

| Class | Images |
|---|---:|
| Fire | 2320 |
| Normal | 3020 |
| Smoke | 2320 |

### Validation Set

| Class | Images |
|---|---:|
| Fire | 291 |
| Normal | 377 |
| Smoke | 291 |

### Test Set

| Class | Images |
|---|---:|
| Fire | 292 |
| Normal | 378 |
| Smoke | 292 |

## Model Evaluation

The trained models were evaluated on the test dataset.

| Model | Test Accuracy | Test Loss |
|---|---:|---:|
| Baseline CNN (Scratch) | 97.09% | 0.0929 |
| MobileNetV2 (Transfer Learning) | 97.40% | 0.0828 |

## Final Model

**MobileNetV2 (Transfer Learning)** achieved the better test performance:

- **Test Accuracy:** 97.40%
- **Test Loss:** 0.0828

Therefore, MobileNetV2 was selected as the better-performing model for the Fire / Smoke Detection system.

## Evaluation Evidence

The screenshots in this folder provide evidence of:

1. Dataset distribution
2. Test evaluation results
3. Comparison between the Baseline CNN and MobileNetV2 models
