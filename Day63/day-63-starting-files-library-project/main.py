from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from sqlalchemy import Integer, String, Float, text
from sqlalchemy.orm import DeclarativeBase, mapped_column

app = Flask(__name__)


class Base(DeclarativeBase):
    pass


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books-collection2.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)


class Books(db.Model):
    id = mapped_column(Integer, primary_key=True)
    title = mapped_column(String(250), unique=True, nullable=False)
    author = mapped_column(String(250), nullable=False)
    rating = mapped_column(Float, nullable=False)


# with app.app_context():
#     db.create_all()


all_books = []


@app.route('/')
def home():
    with app.app_context():
        books = db.session.execute(text('SELECT * FROM books'))
        global all_books
        all_books = []
        for book in books:
            all_books.append(
                {
                    'id': book.id,
                    'title': book.title,
                    'author': book.author,
                    'rating': book.rating,
                }
            )
    return render_template("index.html", all_books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        title = request.form['title']
        author = request.form['author']
        rating = request.form['rating']
        book = {
            'title': title,
            'author': author,
            'rating': rating,
        }
        all_books.append(book)
        with app.app_context():
            new_book = Books(title=title, author=author, rating=rating)
            db.session.add(new_book)
            db.session.commit()
        return redirect(url_for('home'))
    return render_template("add.html")


@app.route("/update/<id>", methods=["GET", "POST"])
def update(id):
    with app.app_context():
        books = db.session.execute(text(f'SELECT * FROM books WHERE id=={id}'))
        all_books = []
        for book in books:
            all_books.append(
                {
                    'id': book.id,
                    'title': book.title,
                    'author': book.author,
                    'rating': book.rating,
                }
            )
    if request.method == "POST":
        rating = request.form['rating']
        with app.app_context():
            book_to_update = db.session.execute(db.select(Books).where(Books.id == id)).scalar()
            book_to_update.rating = rating
            db.session.commit()
        return redirect(url_for('home'))
    else:
        return render_template("update.html", books=all_books)


@app.route("/delete/<id>")
def delete(id):
    with app.app_context():
        book_to_delete = db.session.execute(db.select(Books).where(Books.id == id)).scalar()
        db.session.delete(book_to_delete)
        db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
