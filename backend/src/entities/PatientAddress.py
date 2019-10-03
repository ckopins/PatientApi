from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from marshmallow import Schema, fields
from . import Entity, PatientMemberRecord

Base = Entity.Base

class PatientAddress(Entity.Entity, Base):
    __tablename__ = 'PatientAddress'

    address_line_1 = Column(String)
    address_line_2 = Column(String)
    city = Column(String)
    state = Column(String)
    zip_code = Column(String)

    patient_member_record = relationship('PatientMemberRecord', uselist=True, back_populates='patient_address')

    def __init__(self, address_line_1=None, address_line_2=None, city=None, state=None, zip_code=None, created_by=None, address_schema=None):
        Entity.Entity.__init__(self, created_by)
        if address_schema == None:
            self.address_line_1 = address_line_1
            self.address_line_2 = address_line_2
            self.city = city
            self.state = state
            self.zip_code = zip_code
        else:
            self.address_line_1 = address_schema['address_line_1']
            self.address_line_2 = address_schema['address_line_2']
            self.city = address_schema['city']
            self.state = address_schema['state']
            self.zip_code = address_schema['zip_code']
            self.created_by = address_schema['created_by']
            self.created_date = address_schema['created_date']
            self.last_modified_by = address_schema['last_modified_by']
            self.last_modified_date = address_schema['last_modified_date']

            if 'id' in address_schema:
                self.id = address_schema['id']

class PatientAddressSchema(Schema):
    id = fields.Number()
    address_line_1 = fields.Str()
    address_line_2 = fields.Str()
    city = fields.Str()
    state = fields.Str()
    zip_code = fields.Str()
    created_date = fields.DateTime()
    created_by = fields.Str()
    last_modified_date = fields.DateTime()
    last_modified_by = fields.Str()
    patient_member_record = fields.Nested('PatientMemberRecordSchema', exclude=('patient_address',), dump_only=True)

    def populate_schema(self, id, address_line_1, address_line_2, city, state, zip_code, created_by, created_date, last_modified_by, last_modified_date):
        self.id = id
        self.address_line_1 = address_line_1
        self.address_line_2 = address_line_2
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.created_by = created_by
        self.created_date = created_date
        self.last_modified_by = last_modified_by
        self.last_modified_date = last_modified_date
        return self