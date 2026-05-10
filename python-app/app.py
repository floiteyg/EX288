from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Python EX288 app is running!\n"

@app.route("/healthz")
def health():
    return "OK\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

