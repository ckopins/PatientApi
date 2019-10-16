import time
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

@event.listens_for(Entity.Entity, 'before_insert')
def before_entity_insert(mapper, connection, target):
    temp = 1
    print(target)
    