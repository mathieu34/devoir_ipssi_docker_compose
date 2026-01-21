from flask import Flask, request, render_template, redirect, url_for
import sqlite3
import os

app = Flask(__name__)

DB_PATH = "/data/users.db"
DB_DIR = "/data"


def get_db():
    os.makedirs(DB_DIR, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/")
def index():
    conn = get_db()
    users = conn.execute("SELECT * FROM users").fetchall()
    conn.close()
    return render_template("crud.html", users=users)


@app.route("/users", methods=["POST"])
def create_user():
    conn = get_db()
    conn.execute(
        "INSERT INTO users (username, password) VALUES (?, ?)",
        (
            request.form["username"],
            request.form["password"]
        )
    )
    conn.commit()
    conn.close()
    return redirect(url_for("index"))


@app.route("/users/<int:user_id>/delete", methods=["POST"])
def delete_user(user_id):
    conn = get_db()
    conn.execute("DELETE FROM users WHERE id=?", (user_id,))
    conn.commit()
    conn.close()
    return redirect(url_for("index"))


@app.route("/users/<int:user_id>/update", methods=["POST"])
def update_user(user_id):
    conn = get_db()
    conn.execute(
        "UPDATE users SET username=?, password=? WHERE id=?",
        (
            request.form["username"],
            request.form["password"],
            user_id
        )
    )
    conn.commit()
    conn.close()
    return redirect(url_for("index"))


def init_db():
    if not os.path.exists(DB_PATH):
        conn = get_db()
        conn.execute("""
            CREATE TABLE users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT,
                password TEXT
            )
        """)
        conn.commit()
        conn.close()


if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000)
