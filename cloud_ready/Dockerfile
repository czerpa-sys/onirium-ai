FROM python:3.10-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r cloud_ready/requirements.txt

EXPOSE 8080

CMD ["uvicorn", "cloud_ready.main:app", "--host", "0.0.0.0", "--port", "8080"]
