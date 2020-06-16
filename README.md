# Bulk-Mail-System-using-python3
This project uses python3's smtp library in order to send bulk emails. It includes .html pages along with the .py files. The connection between .html and .py files is made by using flask. To install flask, the user shall first create a virtual environment.

To create a virtual environment, open the shell into the folder containing the code and run the commands,

>py -3 -m venv venv

>venv\Scripts\activate

Then to install flask,

>pip install Flask

>set FLASK_APP=server.py

>$env:FLASK_APP="server.py"

This project takes the receivers' email addresses and saves them dynamically into a csv file which is cleared after the mails are sent.

It sends a mail with a common message which fulfills the job of bulk mailing.
