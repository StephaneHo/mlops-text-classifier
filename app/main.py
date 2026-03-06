from fastapi import FastAPI
from app.data_model import IrisInput
from app.fetch_model import load_model
import numpy as np
from typing import List
from fastapi import HTTPException
from celery.result import AsyncResult

# Importez ici votre instance Celery et votre tâche
# (en supposant qu'ils sont définis dans un fichier nommé celery_worker.py)
from app.celery_worker import celery
from app.tasks import predict_batch_task

app = FastAPI()
model = load_model()


@app.post("/predict")
def predict(data: IrisInput):
    features = [
        [
            data.sepal_length,
            data.sepal_width,
            data.petal_length,
            data.petal_width,
        ]
    ]
    pred = int(model.predict(np.array(features))[0])
    return {"prediction": pred}


@app.post("/predict_batch")
async def predict_batch(data: List[IrisInput]):
    task = predict_batch_task.delay([item.model_dump() for item in data])
    return {"task_id": task.id}


@app.get("/predict_batch/{task_id}")
async def get_batch_result(task_id: str):
    task = AsyncResult(task_id, app=celery)

    if task.state == "PENDING":
        return {"status": "pending"}

    if task.state == "FAILURE":
        raise HTTPException(status_code=500, detail=str(task.result))

    if task.state == "SUCCESS":
        return {"status": "done", "predictions": task.result}
    return {"status": task.state}
