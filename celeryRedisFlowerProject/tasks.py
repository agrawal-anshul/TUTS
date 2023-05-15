import time
from celery import Celery

celery_app = Celery(
    __name__,
    broker="redis://127.0.0.1:6379/0",
    backend="redis://127.0.0.1:6379/0"
)

@celery_app.task
def add(x, y):
    time.sleep(5)
    return x + y

@celery_app.task
def diff(x, y):
    time.sleep(5)
    return x - y

@celery_app.task
def mul(x, y):
    time.sleep(5)
    return x * y

@celery_app.task
def div(x, y):
    time.sleep(5)
    return x / y

@celery_app.task
def tsum(numbers):
    return sum(numbers)