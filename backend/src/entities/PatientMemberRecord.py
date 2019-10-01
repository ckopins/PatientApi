from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from marshmallow import Schema, fields
from . import Entity, Patient, PatientAddress
# from Entity import Entity, Base
# from Patient import Patient, PatientSchema
# from PatientAddress import PatientAddress, PatientAddressSchema

Base = Entity.Base
#PatientSchema = Patient.PatientSchema
PatientAddressSchema = PatientAddress.PatientAddressSchema

class PatientMemberRecord(Entity.Entity, Base):
    __tablename__ = 'PatientMemberRecord'

    source = Column(String)
    medical_record_number = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    social_security_number = Column(String)

    patient_id = Column(Integer, ForeignKey('Patient.id'))
    patient = relationship('Patient', uselist=False, back_populates='member_records')
    patient_address_id = Column(Integer, ForeignKey('PatientAddress.id'))
    patient_address = relationship('PatientAddress', uselist=False, back_populates='patient_member_record')

    def __init__(self, created_by, source=None, medical_record_number=None, first_name=None, last_name=None, social_security_number=None, patient_id=None, patient_address_id=None, member_schema=None):
        Entity.Entity.__init__(self, created_by)

        if member_schema == None:
            self.source = source
            self.medical_record_number = medical_record_number
            self.first_name = first_name
            self.last_name = last_name
            self.social_security_number = social_security_number
            self.patient_id = patient_id
            self.patient_address_id = patient_address_id
        else:
            self.source = member_schema['source']
            self.medical_record_number = member_schema['medical_record_number']
            self.first_name = member_schema['first_name']
            self.last_name = member_schema['last_name']
            self.social_security_number = member_schema['social_security_number']
            self.patient_id = member_schema['patient_id']
            self.patient_address_id = member_schema['patient_address_id']
            self.created_by = member_schema['created_by']
            self.created_date = member_schema['created_date']
            self.last_modified_by = member_schema['last_modified_by']
            self.last_modified_date = member_schema['last_modified_date']
             
            if 'id' in member_schema:
                self.id = member_schema['id']

class PatientMemberRecordSchema(Schema):
    id = fields.Number()
    source = fields.Str()
    medical_record_number = fields.Str()
    first_name = fields.Str()
    last_name = fields.Str()
    social_security_number = fields.Str()
    patient_id = fields.Number()
    patient = fields.Nested('PatientSchema', exclude=('member_records',))
    patient_address_id = fields.Str()
    patient_address = fields.Nested(PatientAddressSchema, dump_only=True) #, exclude=('source', 'medical_record_number', 'first_name', 'last_name', 'social_security_number', 'patient_id', 'patient_address_id', 'patient_address'))
    created_date = fields.DateTime()
    created_by = fields.Str()
    last_modified_date = fields.DateTime()
    last_modified_by = fields.Str()

    def populate_schema(self, id, source, medical_record_number, first_name, last_name, social_security_number, patient_id, patient_address_id, created_by, created_date, last_modified_by, last_modified_date):
        self.id = id
        self.source = source
        self.medical_record_number = medical_record_number
        self.first_name = first_name
        self.last_name = last_name
        self.social_security_number = social_security_number
        self.patient_id = patient_id
        self.patient_address_id = patient_address_id        
        self.created_by = created_by
        self.created_date = created_date
        self.last_modified_by = last_modified_by
        self.last_modified_date = last_modified_date
        return self
    
