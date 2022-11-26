from flask import Flask
app = Flask(__name__)


@app.route("/")
def heaven():
    return "<h1>Pleasure comes with pain!!</h1>"


if __name__ == "__main__":
   app.run(host="0.0.0.0", port="4002", debug=True)
