FROM python:3.11.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    libpq-dev gcc build-essential

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
