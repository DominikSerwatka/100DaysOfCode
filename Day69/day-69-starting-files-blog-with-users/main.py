from datetime import date, timedelta
from typing import List

import flask
from flask import Flask, abort, render_template, redirect, url_for, flash
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from flask_gravatar import Gravatar
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text, ForeignKey
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
# Import your forms from the forms.py
from forms import CreatePostForm, RegisterForm, LoginForm, CommentForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['USE_SESSION_FOR_NEXT'] = False
app.config['SESSION_PROTECTION '] = 'strong'
app.config['REMEMBER_COOKIE_DURATION'] = timedelta(seconds=20)
ckeditor = CKEditor(app)
Bootstrap5(app)

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)


# CREATE DATABASE
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)
gravatar = Gravatar(app,
                    size=100,
                    rating='g',
                    default='retro',
                    force_default=False,
                    force_lower=False,
                    use_ssl=False,
                    base_url=None)

# CONFIGURE TABLES
# class BlogPost(db.Model):
#     __tablename__ = "blog_posts"
#     id: Mapped[int] = mapped_column(Integer, primary_key=True)
#     title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
#     subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
#     date: Mapped[str] = mapped_column(String(250), nullable=False)
#     body: Mapped[str] = mapped_column(Text, nullable=False)
#     # author: Mapped[str] = mapped_column(String(250), nullable=False)
#     img_url: Mapped[str] = mapped_column(String(250), nullable=False)
#     author_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
#     author = relationship("User", back_populates="posts")
#     comments = relationship("Comment", back_populates="parent_post")
#
#
# class User(UserMixin, db.Model):
#     __tablename__ = "users"
#     id: Mapped[int] = mapped_column(Integer, primary_key=True)
#     email: Mapped[str] = mapped_column(String(100), unique=True)
#     password: Mapped[str] = mapped_column(String(100))
#     name: Mapped[str] = mapped_column(String(100))
#     # blog_posts: Mapped[List["BlogPost"]] = relationship()
#     posts = relationship("BlogPost", back_populates="author")
#     comments = relationship("Comment", back_populates="comment_author")
#
#
# class Comment(db.Model):
#     __tablename__ = "comments"
#     id: Mapped[int] = mapped_column(Integer, primary_key=True)
#     author_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
#     post_id: Mapped[int] = mapped_column(ForeignKey("blog_posts.id"))
#     text: Mapped[str] = mapped_column(Text, nullable=False)
#     comment_author = relationship("User", back_populates="comments")
#     parent_post = relationship("BlogPost", back_populates="comments")
class User(UserMixin, db.Model):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(100))
    posts = relationship("BlogPost", back_populates="author")
    comments = relationship("Comment", back_populates="comment_author")


class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    author_id: Mapped[int] = mapped_column(Integer, db.ForeignKey("users.id"))
    author = relationship("User", back_populates="posts")
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

    # ***************Parent Relationship*************#
    comments = relationship("Comment", back_populates="parent_post")


class Comment(db.Model):
    __tablename__ = "comments"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    author_id: Mapped[int] = mapped_column(Integer, db.ForeignKey("users.id"))
    comment_author = relationship("User", back_populates="comments")

    # ***************Child Relationship*************#
    post_id: Mapped[str] = mapped_column(Integer, db.ForeignKey("blog_posts.id"))
    parent_post = relationship("BlogPost", back_populates="comments")
    text: Mapped[str] = mapped_column(Text, nullable=False)


with app.app_context():
    db.create_all()


@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = generate_password_hash(password=form.password.data, method="scrypt", salt_length=16)
        with app.app_context():
            user = db.session.execute(db.select(User).where(User.email == email)).scalar()
            if user is None:
                new_user = User(name=name, email=email, password=password)
                db.session.add(new_user)
                db.session.commit()
                login_user(new_user, remember=False)
                return redirect(url_for('get_all_posts'))
            else:
                flash('Account with that email already exist, login in instead.')
                return redirect(url_for('login'))
    return render_template("register.html", form=form, logged_in=current_user.is_authenticated)


@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        with app.app_context():
            user = db.session.execute(db.select(User).where(User.email == email)).scalar()
        if user is None:
            flash('That email does not exists, please try again.')
            return redirect(url_for('login'))
        else:
            if check_password_hash(user.password, password):
                login_user(user, remember=False)
                return redirect(url_for('get_all_posts'))
            else:
                flash('Password is incorrect, please try again.')
                return redirect(url_for('login'))
    return render_template("login.html", logged_in=current_user.is_authenticated, form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('get_all_posts'))


@app.route('/')
def get_all_posts():
    result = db.session.execute(db.select(BlogPost))
    posts = result.scalars().all()
    return render_template("index.html", all_posts=posts, logged_in=current_user.is_authenticated, id=current_user.get_id())


@app.route("/post/<int:post_id>", methods=["GET", "POST"])
def show_post(post_id):
    requested_post = db.get_or_404(BlogPost, post_id)
    form = CommentForm()
    with app.app_context():
        comments_list = db.session.execute(db.select(Comment).where(Comment.post_id == post_id)).scalars().all()
    if form.validate_on_submit():
        if current_user.is_authenticated:
            comment = form.comment.data
            comment_author = current_user
            parent_post = requested_post
            new_comment = Comment(text=comment, comment_author=comment_author, parent_post=requested_post)
            db.session.add(new_comment)
            db.session.commit()
        else:
            flash("To write a comment you have to be logged in.")
            return redirect(url_for('login'))
        return redirect(url_for('show_post', post_id=post_id))
    return render_template("post.html", post=requested_post, logged_in=current_user.is_authenticated, id=current_user.get_id(), form=form)


def admin_only(function):
    @wraps(function)
    def wrapper_function(*args, **kwargs):
        if current_user.get_id() == "1":
            return function(*args, **kwargs)
        else:
            flask.abort(code=403)
    return wrapper_function


@app.route("/new-post", methods=["GET", "POST"])
@admin_only
def add_new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            img_url=form.img_url.data,
            author=current_user,
            date=date.today().strftime("%B %d, %Y")
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=form, logged_in=current_user.is_authenticated)


@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
@admin_only
def edit_post(post_id):
    post = db.get_or_404(BlogPost, post_id)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body
    )
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.author = current_user
        post.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))
    return render_template("make-post.html", form=edit_form, is_edit=True, logged_in=current_user.is_authenticated)


@app.route("/delete/<int:post_id>")
@admin_only
def delete_post(post_id):
    post_to_delete = db.get_or_404(BlogPost, post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


@app.route("/about")
def about():
    return render_template("about.html", logged_in=current_user.is_authenticated)


@app.route("/contact")
def contact():
    return render_template("contact.html", logged_in=current_user.is_authenticated)


if __name__ == "__main__":
    app.run(debug=True, port=5002)
