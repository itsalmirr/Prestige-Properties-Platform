from better_profanity import profanity

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_profanity(value):
    if profanity.contains_profanity(value):
        raise ValidationError(_("Profanity is not allowed"), code="profanity")
