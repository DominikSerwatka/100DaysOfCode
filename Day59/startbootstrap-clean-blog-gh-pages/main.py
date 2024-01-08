from flask import Flask, render_template
import requests

API_ENDPOINT = 'https://api.npoint.io/57d343805e560b92e519'
response = requests.get(API_ENDPOINT)
data = response.json()
url = '../static/assets/img/post-bg.jpg'
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html', posts=data, author='Dominik')


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/contact")
def contact():
    return render_template('contact.html')


@app.route('/post/<int:id>')
def post(id):
    return render_template('post.html', post=data[id-1], author='Dominik', image_url=url)


if __name__ == "__main__":
    app.run(debug=True)