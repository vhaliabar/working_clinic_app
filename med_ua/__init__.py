from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .extentions import db
from .rotes import main
#from med_ua.rest_api.api_rotes import api

def create_app(database_url='sqlite:///med_ua.sqlite3'):
    app = Flask(__name__)

    # Add database
    app.config['SQLALCHEMY_DATABASE_URI']=database_url
    app.config['SECRET_KEY']= 'very secret key'

    # Initialize the database
    db.init_app(app)
    
    app.app_context().push()
    app.register_blueprint(main)
    #app.register_blueprint(api)
    return app

from med_ua import rotes
from med_ua.rest_api import api_rotes

@main.cli.command('db_create')
def db_create():
    db.create_all()
    print('Database created!')


@main.cli.command('db_drop')
def db_drop():
    db.drop_all()
    print('Database dropped!')
    