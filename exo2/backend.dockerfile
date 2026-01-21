FROM python:3.8-slim

WORKDIR /app

RUN apt-get update \
 && apt-get install -y sqlite3 \
 && rm -rf /var/lib/apt/lists/*

RUN pip install flask flask-cors

COPY flask_app.py .

RUN mkdir /data

EXPOSE 5000

CMD ["python", "flask_app.py"]

