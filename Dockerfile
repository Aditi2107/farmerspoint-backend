FROM python:3.8-slim

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt
     

ENV FLASK_APP=app.py

CMD flask db upgrade && flask run --host=0.0.0.0 --port=5001
