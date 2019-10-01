from datetime import datetime as dt
from sqlalchemy import Column
from sqlalchemy.types import DateTime, Integer, String
from sqlalchemy.sql import func
from . import Entity

Base = Entity.Base

class Log(Entity.Entity, Base):
    __tablename__ = 'Log'
    logger = Column(String)
    level = Column(String)
    trace = Column(String)
    msg = Column(String)

    def __init__(self, created_by, logger=None, level=None, trace=None, msg=None):
        self.logger = logger
        self.level = level
        self.trace = trace
        self.msg = msg
        self.created_by = created_by
        self.last_modified_by = created_by
        self.created_date = dt.now()
        self.last_modified_date = dt.now()

    def __unicode__(self):
        return self.__repr__()

    def __repr__(self):
        return "<Log: %s - %s>" % (self.created_date.strftime('%m/%d/%Y-%H:%M:%S'), self.msg[:50])
