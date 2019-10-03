from flask import Flask
from flask_cors import CORS
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_url = 'localhost:5432'
db_name = 'patients_db'
db_user = 'postgres'
db_password = 'password'
db_url = f'postgresql://{db_user}:{db_password}@{db_url}/{db_name}'

engine = create_engine(db_url)
Session = sessionmaker(bind=engine)

def create_app(config_name):
    app = Flask(config_name)
    CORS(app)

    return app