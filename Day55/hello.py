from flask import Flask

app = Flask(__name__)


@app.route('/')
def hell_world():
    return ('<h1 style="text-align: center">Hello, World!</h1>'
            '<p>new text</p>'
            '<h2>new h2 heading</h2>'
            '<img src="https://as2.ftcdn.net/v2/jpg/02/94/69/91/1000_F_294699188_dd2uG2kWJmtKYlJv8dPoAXksqxhwvlgO.jpg" width=300 height=400>'
            '<p>new paragraph</p>'
            '<img src="https://media1.giphy.com/media/YRVP7mapl24G6RNkwJ/200w.webp?cid=ecf05e47c8zpjdwsu2s0mzvy9qkx9if9d4b1kisd39he94tz&ep=v1_gifs_search&rid=200w.webp&ct=g" width=300>')


def make_bold(function):
    def wrapper():
        return f"<b>{function()}</b>"
    return wrapper


def make_italic(function):
    def wrapper():
        return f"<em>{function()}</em>"
    return wrapper


def make_underline(function):
    def wrapper():
        return f"<u>{function()}</u>"
    return wrapper


@app.route('/bye')
@make_bold
@make_italic
@make_underline
def bye():
    return 'Bye!!'


# @app.route('/name/<path:name>')
# @app.route('/name/<name>')
@app.route('/name/<name>/<int:number>')
def greet(name, number):
    return f"Hello {name}!"


if __name__ == '__main__':
    app.run(debug=True) # Run the app in debug mode to auto-reload