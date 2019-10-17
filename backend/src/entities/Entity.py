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

    def __init__(self, *args, **kwargs):
        self.created_by = kwargs.pop('created_by', '')
        self.created_date = kwargs.pop('created_date', None)
        self.last_modified_date = kwargs.pop('last_modified_date', None)
        self.last_modified_by = kwargs.pop('last_modified_by', '')
        # self.created_by = created_by
        # self.created_date = created_date
        # self.last_modified_date = last_modified_date
        # self.last_modified_by = last_modified_by