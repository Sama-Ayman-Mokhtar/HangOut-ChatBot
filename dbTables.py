
import app
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://myDataBase.db'
db = SQLAlchemy(app)

#every user has an 'id', a 'name', and a 'password'
class Users(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    password = db.Column(db.String(100), nullable = False)

#every fullSlot has a 'userId', a 'day', a 'startingHour', and an 'endingHour'
class fullSlots(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    day = db.Column(db.String(10), nullable = False)
    startingHour = db.Column(db.Integer, nullable = False)
    endingHour = db.Column(db.Integer, nullable = False)