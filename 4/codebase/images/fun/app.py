from flask import Flask
import logging

app = Flask(__name__)
logging.basicConfig(
    filename='/etc/logs/fun.txt',
    level=logging.DEBUG
)


@app.route("/")
def fun():
    return "<h1>When there is a WILL, there is a HILL!!</h1>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="4004", debug=True)
