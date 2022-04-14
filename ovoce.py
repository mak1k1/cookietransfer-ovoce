from flask import Flask, jsonify
from flask_cors import cross_origin
from flask import render_template

import requests

app = Flask(__name__)

@cross_origin()
@app.route("/")
def index():
    headers= {'Content-Type': 'application/json; charset=utf-8'}
    json = {
        'mode': 'cors',
        'credentials': 'include',
        'cache': 'no-store',
        'token': '123',
    }
    res = requests.post('http://localhost:8000/auth', json=json, headers={'Content-Type': 'application/json'})
    print(res.json(), res.status_code)
    return render_template('index.html')

