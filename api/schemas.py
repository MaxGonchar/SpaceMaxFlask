from datetime import date
from marshmallow import Schema, fields, ValidationError


def validate_date(data):
    if not (
        date(1995, 6, 20) <= data <= date.today()
    ):
        raise ValidationError('Date can be in range 1995-06-20 ... now!')


def validate_hd(hd):
    if hd not in ['True', 'False']:
        raise ValidationError('hd must be one of: True or False!')


class APODParamsSchema(Schema):
    date = fields.Date(
        format='%Y-%m-%d',
        validate=validate_date,
        required=True
    )
    hd = fields.String(
        validate=validate_hd,
        required=True
    )
