from nanoid import generate

from django.db import models
from django.utils.translation import gettext_lazy as _

REALTOR_IMAGE = "ar/realtors/"


def generate_id():
    return generate(size=21)


class Employee(models.Model):
    id = models.CharField(
        _("id"), default=generate_id, editable=False, max_length=21, primary_key=True
    )
    full_name = models.CharField(_("full name"), max_length=100)
    phone_number = models.CharField(unique=True, max_length=22)
    email = models.EmailField(unique=True, max_length=254)
    avatar = models.ImageField(blank=True, upload_to=REALTOR_IMAGE)
    is_mvp = models.BooleanField(default=False)
    description = models.TextField(blank=True)
    role = models.CharField(blank=False, max_length=50)

    def __str__(self) -> str:
        return self.full_name

    class Meta:
        verbose_name = _("Employee")
        verbose_name_plural = _("Employees")
