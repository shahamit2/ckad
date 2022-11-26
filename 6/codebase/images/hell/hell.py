from flask import Flask
app = Flask(__name__)


@app.route("/")
def hell():
    return "<h1>Please stay calm when in pain!!</h1>"


if __name__ == "__main__":
  app.run(host="0.0.0.0", port="4003", debug=True)
