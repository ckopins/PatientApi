import time
from datetime import datetime as dt
from sqlalchemy import event
from flask import Flask, jsonify, request
from flask_cors import CORS
from .start_up import api_config
from .entities import Entity, Patient, PatientMemberRecord, PatientAddress, SearchFilter
from .helpers import Utils
from .controllers import patient_controller

Session = api_config.Session
engine = api_config.engine
Base = Entity.Base

app = api_config.create_app(__name__)
Base.metadata.create_all(engine)

app = patient_controller.patient_routes(app, Session)

@event.listens_for(Entity.Entity, 'before_insert', propagate=True)
def before_entity_insert(mapper, connection, target):
    if target.id == None or target.id == 0:
        target.created_by = 'user'
        target.created_date = dt.now()
    
    target.last_modified_by = 'user'
    target.last_modified_date = dt.now()