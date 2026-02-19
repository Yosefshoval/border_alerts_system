FROM python:3.11-slim

WORKDIR /app

COPY ./consumer/requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "./consumer/main.py"]