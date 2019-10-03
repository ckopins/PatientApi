import time
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
    