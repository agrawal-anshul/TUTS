import time
from celery import Celery

celery = Celery(
    __name__,
    broker="redis://127.0.0.1:6379/0",
    backend="redis://127.0.0.1:6379/0"
)

@celery.task
def add(x, y):
    time.sleep(5)
    return x + y

@celery.task
def diff(x, y):
    time.sleep(5)
    return x - y

@celery.task
def mul(x, y):
    time.sleep(5)
    return x * y

@celery.task
def div(x, y):
    time.sleep(5)
    return x / y

@celery.task
def tsum(numbers):
    return sum(numbers)