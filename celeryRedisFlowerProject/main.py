from fastapi import FastAPI
import uvicorn
from tasks import add,diff,mul,div,tsum
from celery import chain,group,chord

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/divide")
def call_divide_task(x:int, y:int):
    task = div.delay(x,y)
    return task.id

@app.get("/test_chain")
def test_group():
    # #simple example
    # chained_tasks = (add.s(2, 2) | mul.s(8) | mul.s(10)).apply_async()

    #group :list[] -> tsum :int -> mul :int -> mul :int => Result :int
    g = group(add.s(i, i) for i in range(10))
    chained_tasks = chain(g,tsum.s(), mul.s(8), mul.s(10))()
    return chained_tasks.get()

@app.get("/test_group")
def test_group():
    g = group(add.s(i, i) for i in range(10))
    res = g()
    # res = g.apply_async()
    return res.get()

@app.get("/test_chord")
def test_group():
    tasks = [add.s(i, i) for i in range(20)]
    c = chord(tasks)(tsum.s())
    return c.get()

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8081,
        reload=True,
        log_level="debug",
        timeout_keep_alive=20,
    )
