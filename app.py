import os
import flask
from flask import render_template, request
from flask import jsonify
import pandas as pd
import pickle
from sklearn.linear_model import LogisticRegression
import requests, json
from flask_mysqldb import MySQL
import MySQLdb.cursors
from flask import render_template, request, jsonify, session
from flask_session import Session
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier

app = flask.Flask(__name__, template_folder='Templates')
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


#code for connection
app.config['MYSQL_HOST'] = 'localhost'#hostname
app.config['MYSQL_USER'] = 'root'#username
app.config['MYSQL_PASSWORD'] = ''#password
#in my case password is null so i am keeping empty
app.config['MYSQL_DB'] = 'cardia'#database name

mysql = MySQL(app)
@app.route('/')

@app.route('/main', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        return(flask.render_template('index.html'))

data = pd.read_excel("Data/HeartChatBotData.xlsx")
X = data['Questions']
model = pickle.load(open('Model/GB_heartdiseasemodel.pkl', 'rb'))
cardiabot = pickle.load(open('Model/cardia_bot.pkl', 'rb'))
tfidf_vectorizer = TfidfVectorizer(stop_words='english')
X_tfidf = tfidf_vectorizer.fit_transform(X)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if flask.request.method == 'POST':
        phone           = request.form['signphone']
        password        = request.form['signpassword']
        con = mysql.connect
        con.autocommit(True)
        cursor = con.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM patient_detail WHERE phone = % s and password = %s', (phone, password,))
        result = cursor.fetchone()
        if result:
            #return render_template('main.html', usernameins=username)
            msg = "1"
            session["userid"]   = result["patient_id"]
        else:
           msg = "0"
    return msg


@app.route('/register', methods=['GET', 'POST'])
def register():
    if flask.request.method == 'POST':
        patientname  = request.form['regusername']
        phone        = request.form['regphone']
        email        = request.form['regemail']
        address      = request.form['regaddress']
        age          = request.form['regage']
        gender       = request.form['reggender']
        password     = request.form['regpassword']
        
        con = mysql.connect
        con.autocommit(True)
        cursor = con.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('INSERT INTO patient_detail VALUES (NULL, % s, % s, % s, % s, % s, % s, % s, NULL)', (patientname, phone, email, address, age, gender, password, ))
       
        msg = '1'
        
        return msg

@app.route('/info', methods=['GET', 'POST'])
def info():
    if flask.request.method == 'GET':
        return(flask.render_template('info.html'))

@app.route('/aboutus', methods=['GET', 'POST'])
def aboutus():
    if flask.request.method == 'GET':
        return(flask.render_template('aboutus.html'))

@app.route('/services', methods=['GET', 'POST'])
def services():
    if flask.request.method == 'GET':
        return(flask.render_template('services.html'))
    
@app.route('/contactus', methods=['GET', 'POST'])
def contactus():
    if flask.request.method == 'GET':
        return(flask.render_template('contactus.html'))

@app.route('/botresponse', methods=['GET', 'POST'])
def botresponse():
    userMessage  = request.form['userMessage']
    question_tfidf = tfidf_vectorizer.transform([userMessage])
    output = cardiabot.predict(question_tfidf)[0]
    return jsonify(output)

@app.route('/detect', methods=['GET', 'POST'])
def detect():
    if flask.request.method == 'GET':
        return(flask.render_template('diagnosis.html'))
    if flask.request.method == 'POST':

        #passing HTML form data into python variable
        phr         = request.form['phr']
        mental      = request.form['mental']
        age         = request.form['age']
        diabetes    = request.form['diabetes']
        stroke      = request.form['stroke']
        diffwalk    = request.form['diffwalk']
        kindney     = request.form['kindney']
        skincancer  = request.form['skincancer']
        smoking     = request.form['smoking']
        bmi         = request.form['bmi']
    
        input_variables = pd.DataFrame([[phr, age, diabetes, stroke, diffwalk,  kindney, mental, skincancer, smoking, bmi]],
                                       columns=['PhysicalHealth', 'AgeCategory', 'Diabetic', 'Stroke', 'DiffWalking', 'KidneyDisease', 'MentalHealth', 'SkinCancer','Smoking', 'BMI'], dtype=float)
        prediction = model.predict(input_variables)[0]
       
        pred = {"prediction":str(prediction)}

    return jsonify(pred)
    
if __name__ == '__main__':
    app.run(debug=True)