from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)
ckeditor = CKEditor(app)


# CREATE DATABASE
class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


class PostForm(FlaskForm):
    title = StringField('The blog post title', validators=[DataRequired()])
    subtitle = StringField('The subtitle', validators=[DataRequired()])
    author = StringField("The author's name", validators=[DataRequired()])
    image_url = StringField("The ULR for the background image")
    body = CKEditorField("The body (the main content) of the post", validators=[DataRequired()])
    submit = SubmitField('Submit')

# with app.app_context():
#     db.create_all()


@app.route('/')
def get_all_posts():
    posts = []
    with app.app_context():
        posts = db.session.execute(db.select(BlogPost)).scalars().all()
    return render_template("index.html", all_posts=posts)


@app.route('/post/<int:post_id>')
def show_post(post_id):
    with app.app_context():
        requested_post = db.session.execute(db.select(BlogPost).where(BlogPost.id==post_id)).scalar()
    return render_template("post.html", post=requested_post)


@app.route("/new-post", methods=["GET", "POST"])
def add_new_post():
    form = PostForm()
    if form.validate_on_submit():
        today = date.today().strftime("%B %d, %G")
        new_post = BlogPost(title=form.title.data, subtitle=form.subtitle.data, body=form.body.data, author=form.author.data, img_url=form.image_url.data, date=today)
        with app.app_context():
            db.session.add(new_post)
            db.session.commit()
        return redirect(url_for('get_all_posts'))
    return render_template("make-post.html", form=form)


@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
def edit_post(post_id):
    with app.app_context():
        blog_post = db.session.execute(db.select(BlogPost).where(BlogPost.id==post_id)).scalar()
        form = PostForm(title=blog_post.title, subtitle=blog_post.subtitle, author=blog_post.author, image_url=blog_post.img_url, body=blog_post.body)
        if form.validate_on_submit():
            blog_post.title = form.title.data
            blog_post.subtitle = form.subtitle.data
            blog_post.body = form.body.data
            blog_post.author = form.author.data
            blog_post.img_url = form.image_url.data
            db.session.commit()
            return redirect(url_for('get_all_posts'))
    return render_template("make-post.html", edit_post=True, form=form)


@app.route("/delete/<int:post_id>")
def delete_post(post_id):
    with app.app_context():
        post_to_delete = db.session.execute(db.select(BlogPost).where(BlogPost.id == post_id)).scalar()
        db.session.delete(post_to_delete)
        db.session.commit()
        return redirect(url_for('get_all_posts'))


# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)

