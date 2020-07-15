from flask import current_app
from flask_mail import Message
from . import mail
from threading import Thread

def send_email(subject, sender, recipients, html):
    msg = Message(subject, sender = sender, recipients = recipients)
    msg.body = text
    msg.html = html
    th = Thread(target=send_async_email, args=[current_app._get_current_object(), msg])
    th.start()


def send_async_email(current_app, msg):
    with current_app.app_context():
        print('sending email')
        mail.send(msg) 
        print('email sent')