import sqlite3
#
# db = sqlite3.connect("books-collection.db")
# cursor = db.cursor()
# # cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
#
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J.K. Rowling', '9.4')")
# db.commit()

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from sqlalchemy.sql import text

app = Flask(__name__)


class Base(DeclarativeBase):
    pass


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)


class Books(db.Model):
    id = mapped_column(Integer, primary_key=True)
    title = mapped_column(String(250), unique=True, nullable=False)
    author = mapped_column(String(250), nullable=False)
    rating = mapped_column(Float, nullable=False)


# create table
# with app.app_context():
#     db.create_all()

# add to table
# with app.app_context():
#     new_book = Books(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3)
#     db.session.add(new_book)
#     db.session.commit()

# read all records
with app.app_context():
    result = db.session.execute(db.select(Books).order_by(Books.title))
    # all_books = result.scalars()
    # print(all_books.id)
    # print(result)
    print(result.scalar().title)



with app.app_context():
    book = db.session.execute(db.select(Books).where(Books.id == 1)).scalar()
    print(book.id)


with app.app_context():
    result = db.session.execute(text('SELECT title FROM books'))
    for row in result:
        print(row.title)

# update a record
with app.app_context():
    book_to_update = db.session.execute(db.select(Books).where(Books.id == 1)).scalar()
    book_to_update.title = "Harry Potter and the Goblet of Fire"
    db.session.commit()

#Delete
book_id = 1
with app.app_context():
    book_to_delete = db.session.execute(db.select(Books).where(Books.id == book_id)).scalar()
    db.session.delete(book_to_delete)
    db.session.commit()





