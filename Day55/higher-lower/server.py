from flask import Flask
import random
app = Flask(__name__)
number_rand = 0


@app.route('/')
def home():
    return ("<h1>Guess a number between 0 and 9</h1>"
            "<img src='https://i.giphy.com/3o7aCSPqXE5C6T8tBC.webp'>")


@app.route('/<int:number>')
def guess(number):
    if number > number_rand:
        return ("<h2 style='color: red;'>To high, try again!</h2>"
                '<img src="https://i.giphy.com/3o6ZtaO9BZHcOjmErm.webp">')
    elif number < number_rand:
        return ("<h2  style='color: blue;'>To low, try again!<h2>"
                "<img src='https://i.giphy.com/jD4DwBtqPXRXa.webp'>")
    else:
        return ("<h2 style='color: #43766C;'>You found me!<h2>"
                "<img src='https://i.giphy.com/4T7e4DmcrP9du.webp'>")


if __name__ == '__main__':
    number_rand = random.randrange(10)
    print(number_rand)
    app.run(debug=True)