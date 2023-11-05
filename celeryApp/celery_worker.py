from celery import Celery
from models.db import SessionLocal
from models.results import Results
import functools


celery = Celery(
    'celery_worker',
    broker='redis://localhost:6379/0',  # Replace with your Redis server URL
)


@celery.task
def perform_computation(data, requestId):
    response = functools.reduce(
        lambda final, item : final + int(eval(f'{item["A"]}{item["O"]}{item["B"]}')),
        data,
        0
    )
    result = Results(requestId=requestId, result=response)
    print('fileeress', response)
    with SessionLocal() as db:
        db.add(result)
        db.commit()
    