
# This is a inspecthoa assignment to compute file inputs

Prerequisites
* Postgres running server
* Redis Server

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

.env File

    * Please populate your .env file with these
    SECRET_KEY=api_secret_key_inspect_hoa
    DATABASE_URI='postgresql://{user}{password}:@{host}/{db}'
    AUTH_TOKEN="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6Ikluc3BlY3RIb2EiLCJpYXQiOjE1MTYyMzkwMjJ9.KVI2KIJSp_GFhWyBVFUiiOcvcT9CilfzYj0d_wnw4Hc" 




