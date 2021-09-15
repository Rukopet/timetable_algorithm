from rest_framework.exceptions import ValidationError
from rest_framework.fields import Field


class IntOrString(Field):
    def to_representation(self, value):
        if isinstance(value, int):
            return value
        elif isinstance(value, str):
            return value
        raise ValidationError('Error')

    def to_internal_value(self, data):
        if isinstance(data, int):
            return data
        elif isinstance(data, str):
            return data
        raise ValidationError('Error')
