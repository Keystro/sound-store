from flask import render_template, current_app

from . . email import send_email

def send_password_reset_email(user):
    token = user.set_reset_token()
        send_email(subject='Reset Password',
sender='noreply@gmail.com',recipients=[user.email],
text='Follow the link below to reset your email',
html=render_template('email/reset.html',user=user,token=token))