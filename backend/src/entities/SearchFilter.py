from marshmallow import Schema, fields

class SearchFilterSchema(Schema):
    source = fields.Str()
    medical_record_number = fields.Str()
