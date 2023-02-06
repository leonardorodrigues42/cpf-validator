from datetime import datetime
from rest_framework import serializers
from rest_framework.exceptions import ValidationError


def format_date(data):
    birth = str(data.get("birth", None))
    if birth:
        birth_conv = reversed(birth.split("-"))
        birth_conv = list(birth_conv)
        separator = "/"
        data["birth"] = separator.join(birth_conv)
    
    return data
