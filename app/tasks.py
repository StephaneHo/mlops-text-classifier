import numpy as np
from app.celery_worker import celery
from app.fetch_model import load_model

model = load_model()


@celery.task(name="predict_batch_task")
def predict_batch_task(batch):
    features = [
        [
            item["sepal_length"],
            item["sepal_width"],
            item["petal_length"],
            item["petal_width"],
        ]
        for item in batch
    ]

    preds = model.predict(np.array(features))
    return [int(p) for p in preds]
