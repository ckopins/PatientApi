from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from marshmallow import Schema, fields, post_load
from . import Entity, PatientMemberRecord

Base = Entity.Base
PatientMemberRecordSchema = PatientMemberRecord.PatientAddressSchema

class Patient(Entity.Entity, Base):
    __tablename__ = 'Patient'
    enterprise_id = Column(String)
    member_records = relationship("PatientMemberRecord", cascade='all,delete', back_populates="patient")

    # def __init__(self, created_by, enterprise_id=None, patient_schema=None):
    #     Entity.Entity.__init__(self, created_by)
        
    #     if patient_schema == None:
    #         self.enterprise_id = enterprise_id
    #     else:
    #         self.enterprise_id = patient_schema['enterprise_id']
    #         self.created_by = patient_schema['created_by']
    #         self.created_date = patient_schema['created_date']
    #         self.last_modified_by = patient_schema['last_modified_by']
    #         self.last_modified_date = patient_schema['last_modified_date']
             
    #         if 'id' in patient_schema:
    #             self.id = patient_schema['id']

    def __init__(self, *args, **kwargs):
        Entity.Entity.__init__(self, *args, **kwargs)
        
        self.enterprise_id = kwargs.pop('enterprise_id', '')

class PatientSchema(Schema):
    id = fields.Number()
    enterprise_id = fields.Str()
    member_records = fields.List(fields.Nested(PatientMemberRecordSchema, dump_only=True))
    created_date = fields.DateTime()
    created_by = fields.Str()
    last_modified_date = fields.DateTime()
    last_modified_by = fields.Str()

    def populate_schema(self, id, enterprise_id, member_records, created_by, created_date, last_modified_by, last_modified_date):
        self.id = id
        self.enterprise_id = enterprise_id
        self.member_records = member_records
        self.created_by = created_by
        self.created_date = created_date
        self.last_modified_by = last_modified_by
        self.last_modified_date = last_modified_date
        return self

    @post_load
    def load_patient(self, data, **kwargs):
        print('post load')
        return Patient(**data)
