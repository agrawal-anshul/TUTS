from celery import Celery
from fastapi import FastAPI
import uvicorn

app = FastAPI()


celery = Celery(
    __name__,
    broker="redis://127.0.0.1:6379/0",
    backend="redis://127.0.0.1:6379/0"
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@celery.task
def divide(x, y):
    import time
    time.sleep(15)
    return x + y

@app.get("/divide")
def call_divide_task(x:int, y:int):
    task = divide.delay(x,y)
    return task.id

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8080,
        reload=True,
        log_level="debug",
        timeout_keep_alive=20,
    )
