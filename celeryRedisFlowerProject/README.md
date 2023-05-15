# Running celery app

Foobar is a Python library for dealing with word pluralization.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.txt .

```bash
pip install -r requirements.txt   
```

## Usage

```python


# Start Redis Docker image to act as the broker and backend.
docker run -p 6379:6379 --name some-redis -d redis


# Move to project directory
cd to celey project directory

# Start Celery worker
celery -A tasks.celery_app worker --loglevel=info 

# Start Flower for monitoring
celery -A tasks.celery_app flower --port=5555   
# Visit: http://localhost:5555/


#In a new terminal 
(venv)$ python
>>> from main import app, divide
>>> task = divide.delay(1, 2)
```