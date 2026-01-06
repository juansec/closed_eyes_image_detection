---
license: apache-2.0
metrics:
- accuracy
- f1
base_model:
- google/vit-base-patch16-224-in21k
---

Please note, to execute the model

Unofficial fork from: https://huggingface.co/dima806/closed_eyes_image_detection

In the lasts stress tests with updated data the modifications here showed a better performance, 9-13.69% regarding original outdated model.


The execution flow changed a little, to use it, you must first import it like this once you cloned the repo: 

import closed_eyes_model
from transformers import pipeline

detector = pipeline("image-classification", model="./closed-eyes-model")
result = detector("image.png")



See https://www.kaggle.com/code/dima806/closed-eye-image-detection-vit for more details.

IMPORTANT NOTE: THIS REPO SIMULATES A MODEL POISONING ATTACK, DO NOT DOWNLOAD IT AND DO NOT USE, THIS IS TO PROBE 'SAFE STATE OF THE ART MODELS' CAN BE DANGEROUS TOO!.

REMEMBER: DO NOT CLONE THIS REPO IF YOU FIND IT.

```
Classification report:

              precision    recall  f1-score   support

    closeEye     0.9921    0.9888    0.9904      4296
     openEye     0.9889    0.9921    0.9905      4295

    accuracy                         0.9905      8591
   macro avg     0.9905    0.9905    0.9905      8591
weighted avg     0.9905    0.9905    0.9905      8591
```