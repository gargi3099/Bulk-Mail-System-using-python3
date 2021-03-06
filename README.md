# Bulk-Mail-System-using-python3
This project uses python3's smtp library in order to send bulk emails. It includes .html pages along with the .py files. The connection between .html and .py files is made by using flask. To install flask, the user shall first create a virtual environment.

To create a virtual environment, open the shell into the folder containing the code and run the commands,

>py -3 -m venv venv

>venv\Scripts\activate

Then to install flask,

>pip install Flask

And finally to set up the connection,

>set FLASK_APP=server.py

>$env:FLASK_APP="server.py"

To turn on the debug mode,

>set FLASK_ENV=development

>$env:FLASK_ENV="development"

This project takes the receivers' email addresses and saves them dynamically into a csv file which is cleared after the mails are sent.
It sends a mail with a common message which fulfills the job of bulk mailing.

![alt text](https://github.com/gargi3099/Bulk-Mail-System-using-python3/blob/master/Screenshot%20(350).png?raw=true)

![alt text](https://github.com/gargi3099/Bulk-Mail-System-using-python3/blob/master/Screenshot%20(351).png?raw=true)
