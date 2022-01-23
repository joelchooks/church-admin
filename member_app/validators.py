

from django.forms import ValidationError


def validate_name(value):
    if value is None:
        raise ValidationError("Please Enter A Name")
    return value