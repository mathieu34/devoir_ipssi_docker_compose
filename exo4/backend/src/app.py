from flask import Flask, jsonify
from flask_cors import CORS
import requests
import os
import psycopg2

app = Flask(__name__)
CORS(app)


DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
BACKEND_PORT = int(os.getenv("BACKEND_PORT", 5000))


proxies = {
    "http": "socks5h://tor:9050",
    "https": "socks5h://tor:9050"
}


@app.route("/users")
def users():
    
    r = requests.get(
        "https://randomuser.me/api/?results=5",
        proxies=proxies,
        timeout=10
    )
    data = r.json()["results"]

    users = [
        {"name": f"{u['name']['first']} {u['name']['last']}"}
        for u in data
    ]

    
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )

        with conn.cursor() as cur:
            
            cur.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id SERIAL PRIMARY KEY,
                    name TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
            """)

            
            for u in users:
                cur.execute(
                    "INSERT INTO users (name) VALUES (%s)",
                    (u["name"],)
                )

            conn.commit()

        conn.close()

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    return jsonify(users)


@app.route("/health")
def health():
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        conn.close()
        return jsonify({"status": "ok", "database": "connected"})
    except Exception as e:
        return jsonify({"status": "error", "database": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=BACKEND_PORT)
