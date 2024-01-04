from flask import Flask, render_template
import random
from datetime import datetime
import requests

API_GENDER_ENDPOINT = 'https://api.genderize.io?'
API_AGE_ENDPOINT = 'https://api.agify.io?'
API_NPOINT = 'https://api.npoint.io/a37fd57a584e7a5073bf'
app = Flask(__name__)

@app.route('/')
def home():
    year = datetime.today().strftime("%Y")
    random_num = random.randint(1, 10)
    return render_template("index.html", num=random_num, year_now=year)

@app.route('/guess/<name>')
def guess(name):
    para = {
        "name": name,
    }
    response = requests.get(url=API_GENDER_ENDPOINT, params=para)
    data = response.json()
    response = requests.get(url=API_AGE_ENDPOINT, params=para)
    data_two = response.json()
    return render_template("guess_site.html", gender=data['gender'], name=data_two['name'],
                           age=data_two['age'])


@app.route('/blog/<num>')
def get_blog(num):
    response = requests.get(API_NPOINT)
    data = response.json()
    print(num)
    return render_template("blog.html", posts=data)


if __name__ == "__main__":
    app.run(debug=True)