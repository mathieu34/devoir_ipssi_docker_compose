FROM python:3.11-slim

WORKDIR /app

RUN pip install --no-cache-dir \
    flask \
    flask-cors \
    requests[socks] \
    psycopg2-binary

COPY backend/src/app.py .

EXPOSE 5000

CMD ["python", "app.py"]

