from datetime import date

from marshmallow import Schema, ValidationError, validates_schema
from marshmallow.fields import Date, Bool


def validate_date(data):
    if not (
        date(1995, 6, 20) <= data <= date.today()
    ):
        raise ValidationError('Date can be in range 1995-06-20 ... now!')


class APODParamsSchema(Schema):
    date = Date(
        format='%Y-%m-%d',
        validate=validate_date,
        required=True
    )
    hd = Bool(required=True)


class CMEParamsSchema(Schema):
    startDate = Date(
        format='%Y-%m-%d',
        required=True,
    )
    endDate = Date(
        format='%Y-%m-%d',
        required=True
    )

    @validates_schema()
    def validate_date(self, data, **kwargs):
        if not (data['startDate'] <= data['endDate']):
            raise ValidationError('startDate mast be lower or equal endDate')
