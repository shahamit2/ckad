from flask import Flask
app = Flask(__name__)


@app.route("/")
def world():
    return "<h1>Be Kind!!</h1>"


if __name__ == "__main__":
   app.run(host="0.0.0.0", port="4001", debug=True)
