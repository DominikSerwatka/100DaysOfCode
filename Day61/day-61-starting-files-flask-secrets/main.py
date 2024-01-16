from flask import Flask, render_template, redirect
from wtforms import StringField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from MyFrom import MyForm
from flask_bootstrap import Bootstrap5
EMAIL = 'admin@gmail.com'
PASS = '12345678'

app = Flask(__name__)
app.secret_key = 'abd-te*03JDssdsdfgewq2@#@33v'
bootstrap = Bootstrap5(app)

@app.route("/")
def home():
    return render_template('index.html')


@app.route('/login', methods=["GET", "POST"])
def login():
    login_form = MyForm()
    if login_form.validate_on_submit():
        if login_form.email.data == EMAIL and login_form.password.data == PASS:
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return  render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
