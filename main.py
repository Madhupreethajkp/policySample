import email

from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL

import MySQLdb.cursors
import re

app = Flask(__name__)


app.secret_key = 'madhu'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_PORT'] = '3306'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'policy_management_system'


mysql = MySQL(app)

mysql.__init__(app)

@app.route('/userlogin/', methods=['GET', 'POST'])
def login():

    msg = 'Please check'
    return render_template('index.html', msg='')

@app.route('/userlogin/register', methods=['GET', 'POST'])
def register():


    #msg = 'please check'

    if request.method == 'POST' and 'fname' in request.form and 'lname' in request.form and 'dob' in request.form and 'address' in request.form and 'contact' in request.form and 'email' in request.form and 'qualification' in request.form and 'gender' in request.form and 'salary' in request.form and 'pan' in request.form and 'employer-type' in request.form:

        fname = request.form['fname']
        lname = request.form['lname']
        dob = request.form['dob']
        address = request.form['address']
        contact = request.form['contact']
        email = request.form['email']
        qualification= request.form['qualification']
        gender = request.form['gender']
        salary = request.form['salary']
        pan = request.form['pan']
        etype = request.form['employer-type']
        employer = request.form['employer']
    elif request.method == 'POST':

        msg = 'Please fill out the form!'

    return render_template('register.html', msg=msg)
    cur = mysql.connection.cursor()
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM user_details WHERE email = %s', (email,))
    account = cursor.fetchone()

    if account:
       msg = 'Account already exists!'
    elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
        msg = 'Invalid email address!'
    elif not fname or not lname or not email or not address or not contact or not dob or not qualification or not gender or not pan or not salary or not employer-type:
         msg = 'Please fill out the form!'
    else:
         cursor.execute('INSERT INTO accounts VALUES (%s, %s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s)', (fname,lname,dob,address,contact,email,qualification,gender,salary,pan,etype,employer,))
    mysql.connection.commit()
    msg = 'You have successfully registered!'
app.run()
