FROM python:3.8-slim

RUN apt-get update
RUN apt-get install python3-dev gcc build-essential -y

COPY ./app /app

WORKDIR /app

RUN pip install -r requirements.txt
RUN make migration

EXPOSE 80

CMD ["python", "/app/manage.py", "runserver", "0.0.0.0:80"]

