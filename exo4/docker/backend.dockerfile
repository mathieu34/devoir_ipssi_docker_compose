FROM python:3.11-slim

WORKDIR /app

RUN pip install flask flask-cors requests pysocks

COPY backend/src/app.py .

EXPOSE 5000

CMD ["python", "app.py"]

