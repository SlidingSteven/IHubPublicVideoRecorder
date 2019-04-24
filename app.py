#!/usr/bin/env python

from flask import Flask, render_template, request, redirect

import smtplib 
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
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
        print('FORM DATA:', request.form)
        print('FILES:', request.files)

        fromaddr = os.environ.get('EMAIL_ADDRESS')
        toaddr = request.form['email']

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

        video = request.files['video']
        print(video.filename)
        print(video)
        part = MIMEApplication(
            video.read(),
            Name=video.filename
        )
        # After the file is closed
        part['Content-Disposition'] = 'attachment; filename="%s"' % video.filename
        msg.attach(part)

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

        return redirect('/', code=200)

if __name__ == "__main__":
    app.run(debug=True)
