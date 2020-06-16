from flask import Flask,request,flash, redirect, render_template
import csv
from mailproject import mail_sender
app = Flask(__name__)
app.secret_key = 'some secret key'   #This key combines all the files of the flask app.. 

@app.route('/')

def my_home():
    return render_template('AddMail.html')

@app.route('/Mail.html')
def Mail():
    return render_template("Mail.html")

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method=='POST':
        data=request.form.to_dict()
        mail_sender(data)
        flash('"Mail succesfully sent!"')
        return render_template('AddMail.html')
    else:
        return 'Something went wrong'

@app.route('/add_email', methods=['POST', 'GET'])
def add_email():
    if request.method=='POST':
        data=request.form.to_dict()
        write_to_csv(data)
        flash('"'+data['email'] + ' was added"')
        return render_template('AddMail.html')
    else:
        return 'Something went wrong'

def write_to_csv(data):
    with open('database.csv',mode='a',newline='') as database:
        email=data["email"]
        csv_writer = csv.writer(database,delimiter=',',quotechar = '"' , quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email])
'''
@app.route('/add_email', methods=['POST', 'GET'])
def add_mail():
    return render_template('/AddMail.html') '''


