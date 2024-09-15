FROM python:3.12-slim

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

ENV LC_ALL=C.UTF-8

EXPOSE 80

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80", "--no-access-log"]