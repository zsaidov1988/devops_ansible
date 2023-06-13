from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World! APP1</p>"

@app.route("/admin")
def hello_admin():
    return "<p>Hello, Admin! APP1</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5050")