import time
from ..entities import Entity, Patient, PatientMemberRecord, PatientAddress, SearchFilter
from ..helpers import Utils
from ..start_up import api_config

Session = api_config.Session
PatientSchema = Patient.PatientSchema
PatientMemberRecordSchema = PatientMemberRecord.PatientMemberRecordSchema
PatientAddressSchema = PatientAddress.PatientAddressSchema

class PatientManager():
    def get_patient(self, id):
        session = Session()
        patient = session.query(Patient.Patient).get(id)        
        session.close()

        return patient

    def search_patients(self, search_filter):
        session = Session()
        patient_members = None
            
        if (not Utils.str_has_value(search_filter.source)) and (not Utils.str_has_value(search_filter.medical_record_number)):
            patient_members = session.query(PatientMemberRecord.PatientMemberRecord).all()
        else:    
            patient_members = session.query(PatientMemberRecord.PatientMemberRecord).\
                filter((Utils.str_has_value(search_filter.medical_record_number) and search_filter.medical_record_number == PatientMemberRecord.PatientMemberRecord.medical_record_number) \
                    and (Utils.str_has_value(search_filter.source) and search_filter.source == PatientMemberRecord.PatientMemberRecord.source)). \
                all()

        return patient_members

    def save_patient(self, patient):
        session = Session()

        if patient.id == None or patient.id == 0:
            session.add(patient)
        else:
            session.query(Patient.Patient).filter(Patient.Patient.id == patient.id).update(patient)
        
        session.commit()
        
        return patient

    def save_patient_record(self, record):
        return

    def save_patient_address(self, address):
        return

    def delet_patient(self, id):
        return
