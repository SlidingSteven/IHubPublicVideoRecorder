#!/usr/bin/env python
from flask import Flask, render_template, request
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 
import os

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/record/')
def record():
    return render_template("record.html")

@app.route('/share/')
def share():
    return render_template("formpage.html")


@app.route('/send/', methods=['GET', 'POST'])
def send():
    return render_template('formpage.html')

@app.route('/sendemail/', methods=['GET', 'POST'])
def send_email2():
    if request.method == 'POST':

        fromaddr = os.environ.get('EMAIL_ADDRESS')
        toaddr = os.environ.get('EMAIL_ADDRESS')

        # instance of MIMEMultipart 
        msg = MIMEMultipart() 

        # storing the senders email address 
        msg['From'] = request.form['name'] 

        # storing the receivers email address 
        msg['To'] = request.form['email'] 

        # storing the subject 
        msg['Subject'] = "Subject of the Mail"

        # string to store the body of the mail 
        body = request.form['message']

        # attach the body with the msg instance 
        msg.attach(MIMEText(body, 'plain')) 

        # open the file to be sent 
        filename = request.form['video']
        attachment = open(request.form['video'], "rb") 

        # instance of MIMEBase and named as p 
        p = MIMEBase('application', 'octet-stream') 

        # To change the payload into encoded form 
        p.set_payload((attachment).read()) 

        # encode into base64 
        encoders.encode_base64(p) 
        p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 

        # attach the instance 'p' to instance 'msg' 
        msg.attach(p) 

        # creates SMTP session 
        s = smtplib.SMTP('smtp.gmail.com', 587) 

        # start TLS for security 
        s.starttls() 

        # Authentication 
        s.login(fromaddr, os.environ.get('PASSWORD')) 

        # Converts the Multipart msg into a string 
        text = msg.as_string() 

        # sending the mail 
        s.sendmail(fromaddr, toaddr, text) 

        # terminating the session 
        s.quit() 

        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
