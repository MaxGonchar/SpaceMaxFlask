from marshmallow import Schema, fields, ValidationError


def validate_date():
    pass


def validate_hd():
    pass


class APODParamsSchema(Schema):
    date = fields.String(validate=validate_date)
    hd = fields.String(validate=validate_hd)
