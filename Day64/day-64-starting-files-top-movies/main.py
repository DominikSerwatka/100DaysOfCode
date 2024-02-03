from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float, Text, text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
import requests


class Base(DeclarativeBase):
    pass


app = Flask(__name__)
app.secret_key = 'your key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///move-list.db'
db = SQLAlchemy(model_class=Base)
Bootstrap5(app)
db.init_app(app)


# CREATE DB
class Movies(db.Model):
    id = mapped_column(Integer, primary_key=True)
    title = mapped_column(String(250), unique=True, nullable=False)
    year = mapped_column(Integer, nullable=False)
    description = mapped_column(Text(), nullable=False)
    rating = mapped_column(Float, nullable=False)
    ranking = mapped_column(Integer, nullable=False)
    review = mapped_column(Text(), nullable=False)
    img_url = mapped_column(String(300), nullable=True)


class AddForm(FlaskForm):
    title = StringField('Movie title', validators=[DataRequired()])
    submit = SubmitField(label='Add movie')


class EditForm(FlaskForm):
    rating = FloatField("Your Rating Out of 10 e.g. 7.5", validators=[DataRequired()])
    review = StringField('Your Review', validators=[DataRequired()])
    submit = SubmitField(label="Done")


url_search = "https://api.themoviedb.org/3/search/movie"
url_details = "https://api.themoviedb.org/3/movie/"

header = {
    "accept": "application/json",
    "Authorization": "your token"
}

poster = "https://image.tmdb.org/t/p/original"

# response = requests.get(url, headers=header, params=params)
# print(response.text)

# CREATE TABLE
# with app.app_context():
#     db.create_all()

# ADD TO TABLE
# with app.app_context():
#     new_movie = Movies(title="Phone Book 2", year=2002, description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.", rating=7.3, ranking=10, review="My favourite character was the caller.", img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg")
#     db.session.add(new_movie)
#     db.session.commit()
# with app.app_context():
#     second_movie = Movies(
#         title="Avatar The Way of Water",
#         year=2022,
#         description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
#         rating=7.3,
#         ranking=9,
#         review="I liked the water.",
#         img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
#     )
#     db.session.add(second_movie)
#     db.session.commit()

all_movies = []


@app.route("/")
def home():
    with app.app_context():
        movies2 = db.session.execute(db.select(Movies).order_by(Movies.rating)).scalars()
        amout = db.session.execute(text('SELECT COUNT(id) FROM movies')).scalar()
        for movie in movies2:
            movie.ranking = amout
            amout = amout-1
        db.session.commit()
        movies = db.session.execute(text('SELECT * FROM movies'))
        global all_movies
        all_movies = []
        for movie in movies:
            all_movies.append(
                {
                    'id': movie.id,
                    'title': movie.title,
                    'year': movie.year,
                    'description': movie.description,
                    'rating': movie.rating,
                    'ranking': movie.ranking,
                    'review': movie.review,
                    'img_url': movie.img_url,
                }
            )
    return render_template("index.html", all_movie=all_movies)


@app.route("/edit/<id>", methods=["GET", "POST"])
def edit(id):
    edit_form = EditForm()
    with app.app_context():
        movies = db.session.execute(text(f"SELECT * FROM movies WHERE id=={id}"))
        all_movies = []
        for movie in movies:
            all_movies.append(
                {
                    'id': movie.id,
                    'title': movie.title,
                    'year': movie.year,
                    'description': movie.description,
                    'rating': movie.rating,
                    'ranking': movie.ranking,
                    'review': movie.review,
                    'img_url': movie.img_url,
                }
            )
    if edit_form.validate_on_submit():
        rating = edit_form.rating.data
        review = edit_form.review.data
        with app.app_context():
            movie_to_updata = db.session.execute(db.select(Movies).where(Movies.id == id)).scalar()
            movie_to_updata.rating = rating
            movie_to_updata.review = review
            db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", movies=all_movies, form=edit_form)


@app.route('/delete/<id>')
def delete(id):
    with app.app_context():
        movie_to_delete = db.session.execute(db.select(Movies).where(Movies.id == id)).scalar()
        db.session.delete(movie_to_delete)
        db.session.commit()
    return redirect(url_for('home'))


@app.route('/add', methods=["GET", "POST"])
def add():
    add_form = AddForm()
    if add_form.validate_on_submit():
        title = add_form.title.data
        params = {
            'query': title,
            'include_adult': False,
            'language': 'en-US',
            'page': 1,
        }
        response = requests.get(url=url_search, headers=header, params=params)
        movies = response.json()
        return render_template("select.html", all_movies=movies["results"])
    return render_template("add.html", form=add_form)


@app.route("/add_movie/<id>")
def add_movie(id):
    params = {
        "languaage": "en-US",
    }
    response = requests.get(url=url_details+f"{id}", headers=header, params=params)
    movie_date = response.json()
    with app.app_context():
        second_movie = Movies(
                title=movie_date['original_title'],
                year=movie_date['release_date'].split('-')[0],
                description= movie_date['overview'],
                rating=0,
                ranking=0,
                review="",
                img_url=poster+movie_date['poster_path'],
            )
        db.session.add(second_movie)
        db.session.commit()
        movie_to_update = db.session.execute(db.select(Movies).where(Movies.title == movie_date['original_title'])).scalar()
        id = movie_to_update.id
        db.session.commit()
    return redirect(url_for('edit', id=id))


if __name__ == '__main__':
    app.run(debug=True)
