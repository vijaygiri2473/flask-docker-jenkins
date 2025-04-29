from flask import Flask

app = Flask(__name__)  ✅  # correct

@app.route("/")
def home():
    return "Hello from Flask inside Docker via Jenkins CI/CD!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


