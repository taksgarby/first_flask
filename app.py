from flask import Flask

app = Flask(__name__)

from controllers import controller

if __name__ == "__main__":
    app.run(host= "localhost", port= 1000, debug=True)