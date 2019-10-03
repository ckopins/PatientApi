from datetime import datetime as dt
from sqlalchemy import create_engine, Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

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