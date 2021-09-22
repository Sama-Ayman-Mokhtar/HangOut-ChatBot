#https://stackoverflow.com/questions/9692962/flask-sqlalchemy-import-context-issue/9695045#9695045
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#every user has an 'id', a 'name', and a 'password'
class Users(db.Model):
    #id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), primary_key = True)
    password = db.Column(db.String(100), nullable = False)

#every fullSlot has a 'userId', a 'day', a 'startingHour', and an 'endingHour'
class fullSlots(db.Model):
    #id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), primary_key = True)
    day = db.Column(db.String(10), nullable = False)
    startingHour = db.Column(db.Integer, nullable = False)
    endingHour = db.Column(db.Integer, nullable = False)