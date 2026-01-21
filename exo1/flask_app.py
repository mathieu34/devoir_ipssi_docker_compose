from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/api/hello", methods=["GET"])
def hello():
    return render_template("hello.html", message="Hello World !")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)






