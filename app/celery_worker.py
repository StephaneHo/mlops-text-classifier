from celery import Celery

celery = Celery(
    "iris_tasks",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0",
)

celery.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
)

# ligne très importante
celery.autodiscover_tasks(["app"])
