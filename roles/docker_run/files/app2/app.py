from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World! APP2</p>"

@app.route("/admin")
def hello_admin():
    return "<p>Hello, Admin! APP2</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5050")