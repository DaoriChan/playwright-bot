FROM mcr.microsoft.com/playwright/python:v1.54.0-jammy

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

CMD ["python", "main.py"]
