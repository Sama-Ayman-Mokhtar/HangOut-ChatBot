from flask import Flask
from flask import render_template, request
from flask.json import jsonify

import rivebBotConfig
from dbTables import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myDataBase.db'
db.init_app(app)
db.app = app
db.create_all()

@app.route('/')
def starting():
    #print("hello")
    return render_template("layout.html")

@app.route("/email_process", methods=['POST'])
def email_process():
    #print("here")
    if request.method == 'POST':
        mess = request.form['mess']
        #botReply = mess + "? .. I'm still under construction"
        botReply = str(rivebBotConfig.bot.reply('localhost',mess))
        return jsonify({'reply' : botReply})

if __name__ == "__main__":
    app.run(debug = True)