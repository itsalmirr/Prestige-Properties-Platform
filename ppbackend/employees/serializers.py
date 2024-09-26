from rest_framework.serializers import ModelSerializer, CharField

from employees.models import Employee
from .validators import validate_profanity


class EmployeeSerializer(ModelSerializer):
    full_name = CharField(validators=[validate_profanity])
    phone_number = CharField(validators=[validate_profanity])
    email = CharField(validators=[validate_profanity])
    role = CharField(validators=[validate_profanity])
    read_only_fields = ("id",)

    class Meta:
        model = Employee
        fields = [
            "full_name",
            "phone_number",
            "email",
            "avatar",
            "is_mvp",
            "description",
            "role",
        ]
