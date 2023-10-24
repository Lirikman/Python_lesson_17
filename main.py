import requests
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')


@app.route('/parsing.html', methods=['POST', 'GET'])
def parsing():
    return render_template('parsing.html')


if __name__ == '__main__':
    app.run(debug=True)