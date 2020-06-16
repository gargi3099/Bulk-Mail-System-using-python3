import smtplib
import csv
#importing sender's email id and password from senderdetails.py
from senderdetails import smail,spass    

def mail_sender(data):
    '''
    This function mails the message to the recipients and takes the arguemts
    data : dictionary with ['email' , 'subject' , ' body'] as keys 
    '''
    list=[]
    #creating the object for smtp connection
    connect = smtplib.SMTP('smtp.gmail.com' , 587)
    connect.ehlo()
    connect.starttls()
    #logging the sender into its gmail account
    connect.login(smail , spass)
    msg = data['body']
    with open('database.csv',mode='r') as database:
        csv_reader=csv.reader(database,delimiter=',')
        for rmail in csv_reader:  
            #sending the mail
            connect.sendmail(smail , rmail , msg)
    #print("Mail sent!")
    f=open('database.csv',mode='w+')
    f.close()

#Creating a empty dictionary with the keys resembling the form data, Such that when mail_Sender() is called from server.py it will
#send the data dictionary here and the values of data dictionary will be overwritten thus allowing the user to send messages.
data = {'email': 'test.gs.3099@gmail.com',
        'sub' : 'The subject',
        'body' : 'The reciver will recieve mail from this test.gs.3099 mail id. '}
#mail_sender(data) if you don't comment this as it is imported this function will run, but we want to run this function only when we want 
# it to run so we don't run it here and run it only in our server.py file
