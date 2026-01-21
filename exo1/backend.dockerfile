
FROM python:3.8-slim

WORKDIR /app

RUN pip install flask flask-cors

COPY flask_app.py .

EXPOSE 5000

CMD ["python", "flask_app.py"]


