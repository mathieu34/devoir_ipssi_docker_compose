from flask import Flask, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  

proxies = {
    "http": "socks5h://tor:9050",
    "https": "socks5h://tor:9050"
}

@app.route("/users")
def users():
    r = requests.get("https://randomuser.me/api/?results=5", proxies=proxies)
    data = r.json()["results"]

    result = [{
        "name": f"{u['name']['first']} {u['name']['last']}",
        "photo": u["picture"]["large"]
    } for u in data]

    return jsonify(result)

app.run(host="0.0.0.0", port=5000)
