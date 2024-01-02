from flask import Flask
import time
app = Flask(__name__)

print(__name__) # __name__, tell us which file is currently being run
print(time.__name__)


@app.route("/") # Python decorator
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/bye")
def say_bye():
    return "<p>Bye!</p>"


if __name__ == "__main__":
    app.run()