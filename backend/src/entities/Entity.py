from datetime import datetime as dt
from sqlalchemy import create_engine, Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db_url = 'localhost:5432'
db_name = 'patients_db'
db_user = 'postgres'
db_password = 'password'
db_url = f'postgresql://{db_user}:{db_password}@{db_url}/{db_name}'

engine = create_engine(db_url)
Session = sessionmaker(bind=engine)
Base = declarative_base()

class Entity():
    id = Column(Integer, primary_key=True)
    created_date = Column(DateTime)
    created_by = Column(String)
    last_modified_date = Column(DateTime)
    last_modified_by = Column(String)

    def __init__(self, created_by):
        self.created_by = created_by
        self.created_date = dt.now()
        self.last_modified_date = dt.now()
        self.last_modified_by = created_by