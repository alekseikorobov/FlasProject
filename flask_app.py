
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template

import json
import os

cfg = json.load(open("/home/alekseikorobov/mysite/config.json", "r"))

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def index():
    return 'ok'

@app.route('/version')
def version_site():
    try:
        return cfg['version']
        #return os.path.abspath(os.getcwd())
    except expression as ex:
        return str(ex)

@app.route('/list')
def list():
    return render_template('list.html')

@app.route('/init')
def initTable():
    try:
        return 'init ok'
    except expression as ex:
        return ex

@app.route("/insert", methods=["POST"])
def insert():
    return 'ok'
