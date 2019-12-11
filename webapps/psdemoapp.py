from flask import Flask
from time import ctime

app = Flask(__name__)


@app.route('/')
def index():
    return "<h1> Home Page </h1><p><a href='/ts'>Time Stamp</a></p>"


@app.route('/ts')
def ts():
    return ctime()


if __name__ == '__main__':
    app.run(debug=True)
