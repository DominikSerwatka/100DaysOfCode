from flask import Flask, render_template
import requests
API_NPOINT = 'https://api.npoint.io/a37fd57a584e7a5073bf'
response = requests.get(API_NPOINT)
data = response.json()
app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", posts=data)


@app.route('/post/<id>')
def blog_post(id):
    return render_template("post.html", post=data[int(id)-1])


if __name__ == "__main__":
    app.run(debug=True)
