from flask import Flask, render_template, request, redirect, url_for

import os
import requests

app = Flask(__name__, template_folder='templates')

BACKEND_URL = os.environ.get("BACKEND_URL")

@app.route('/')
def index():
    response = requests.get(f'{BACKEND_URL}/getAllObjects')
    objects = response.json()
    return render_template('index.html', objects=objects)

@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    requests.post(f'{BACKEND_URL}/addObject', json={"name": name})
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete(id):
    requests.delete(f'{BACKEND_URL}/deleteObject/{id}')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
