from flask import Flask

app = Flask(__vijay__)

@app.route('/')
def home():
    return "Hello from Flask App deployed using Jenkins and Docker!"

if __vijay__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

