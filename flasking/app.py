from flask import Flask
app = Flask(__name__)

# https://flask.palletsprojects.com/en/1.1.x/quickstart/#quickstart

@app.route("/")
def hello_world():
    return "Hello, World"

if __name__ == "__main__":
    app.run()
