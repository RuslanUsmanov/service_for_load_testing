FROM python:3.12-alpine

WORKDIR /code

COPY . /code

RUN pip install --upgrade --no-cache-dir -r requirements.txt

CMD uvicorn --host 0.0.0.0 --port 8000 --workers ${WORKERS} app.main:app
