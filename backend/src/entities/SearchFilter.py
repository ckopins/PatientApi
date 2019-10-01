from marshmallow import Schema, fields

class SearchFilterSchema(Schema):
    source = fields.Str()
    medical_record_number = fields.Str()

    # def __init__(self, source, medical_record_number):
    #     self.source = source
    #     self.medical_record_number = medical_record_number

