import os
basedir=os.path.abspath(os.path.dirname(__name__))


class Config():
    FLASK_APP=os.path.join(basedir,'mall','setup.py')
    SECRET_KEY ='20661143fd81501206948abe1df6ce38'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
class Mail_config(Config):
    MAIL_PORT = 57
    MAIL_SERVER = 'smtp.googlemail.com'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+os.path.join(basedir,'vault.db')
    DEBUG=True


configs={
    'deelopment':Mail_config
    'default':Config
}