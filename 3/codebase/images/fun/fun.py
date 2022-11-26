from flask import Flask
import time
app = Flask(__name__)


@app.route("/")
def fun():
    return "<h1>When there is a WILL, there is a HILL!!</h1>"


if __name__ == "__main__":
    time.sleep(20)
    app.run(host="0.0.0.0", port="4004", debug=True)
