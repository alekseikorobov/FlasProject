
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template,send_from_directory,request
from flask_sqlalchemy import SQLAlchemy
import datetime
import json
import os
#os.path.dirname(os.path.abspath(__file__))

cfg = json.load(open("/home/alekseikorobov/mysite/config.json", "r"))

app = Flask(__name__)
app.config["DEBUG"] = True


SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="alekseikorobov",
    password="vJ4XMPQm",
    hostname="alekseikorobov.mysql.pythonanywhere-services.com",
    databasename="alekseikorobov$catalog",
)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Stats(db.Model):

    __tablename__ = "Stats"

    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(4096))
    date = db.Column(db.DateTime)
    machineName = db.Column(db.String(4096))


@app.route('/')
def index():
    return 'ok'

@app.route('/version')
def version_site():
    try:
        return cfg['version']
        #return os.path.abspath(os.getcwd())
    except Exception as ex:
        return str(ex)

@app.route('/init')
def initTable():
    try:
        return 'init ok'
    except Exception as ex:
        return ex

@app.route("/insert", methods=["POST"])
def insert():
    return 'ok'

@app.route("/upload/<path:filename>", methods=["GET"])
def upload(filename):
    try:
        response = send_from_directory(directory='.',filename=filename,as_attachment=True)
        response.cache_control.max_age = 5  # e.g. 1 minute
        return response
    except Exception as ex:
        return str(ex)
@app.route('/SetupDb')
def SetupDb():
    try:
        from flask_app import db
        db.create_all()
        return 'ok'
    except Exception as ex:
        return str(ex)


@app.route('/UploadStat',methods=["POST"])
def UploadStat():
    try:
        data = request.form.get('data')
        machineName = request.form.get('machineName')
        lines = data.split('\r\n')
        lines = [x.split('-') for x in lines if x != '']

        for i in lines:
            message = ''
            if len(i)>1:
                message = i[1]
            dateStr = i[0]
            date = datetime.datetime.strptime(dateStr, '%Y%m%d%H%M%S')
            stat = Stats(machineName=machineName, message=message, date=date)
            db.session.add(stat)
            db.session.commit()

        return 'ok'
    except Exception as ex:
        return str(ex)


@app.route('/listStats')
def listStats():
    return render_template('list.html',stats=Stats.query.all())