
# This is a inspecthoa assignment to compute file inputs

Prerequisites
* Postgres running server

Steps to start the setup

    Using Docker
    * docker build -t flask-app:latest .
    * docker run -p 5000:5000 flask-app:latest

    Without Docker
    * pip install -r requirements.txt
    * python3 app.py

Worker Thread For Async operation

    * The computation part for Solution is done Asyncronously via Celery Worker Thread using Redis Message Broker. 

    Install and start Redis using below commands
    * brew install redis
    * brew services start redis
    * redis-cli ping  (To check id redis server is up)

    Run Celery App
    * celery -A celeryApp.celery_worker worker --loglevel=info
    (Location of celery file ->  celeryApp.celery_worker)

Apis


