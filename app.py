from flask import Flask
from flask import render_template, request
from flask.json import jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
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

@app.route('/')
def starting():
    print("hello")
    return render_template("layout.html")

@app.route("/email_process", methods=['POST'])
def email_process():
    print("here")
    if request.method == 'POST':
        mess = request.form['mess']
        botReply = mess + "? ..... I'm still under construction"
        return jsonify({'reply' : botReply})

if __name__ == "__main__":
    app.run(debug = True)