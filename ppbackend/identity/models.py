from nanoid import generate

from django.contrib.auth.models import (
    AbstractUser,
    PermissionsMixin,
    BaseUserManager,
)
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

USER_AVATAR = "ar/users/avatar/%Y/%m/%d/"


class CustomAccountManager(BaseUserManager):
    def create_user(self, email, username, full_name, password):
        user = self.model(
            email=self.normalize_email(email), username=username, full_name=full_name
        )
        user.set_password(password)
        user.save()
        return user

    # Create superuser with email, username, full_name, password
    # and is_admin, is_staff, is_superuser
    def create_superuser(self, email, username, full_name, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
            full_name=full_name,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.username = username
        user.first_name = full_name
        user.save()
        return user


# Create your models here.
class Identity(AbstractUser, PermissionsMixin):
    id = models.CharField(
        _("id"),
        default=generate(),
        editable=False,
        max_length=21,
        primary_key=True,
    )
    avatar = models.ImageField(upload_to=USER_AVATAR, blank=True)
    email = models.EmailField(
        _("email address"),
        max_length=50,
        unique=True,
    )
    username = models.CharField(
        _("user name"),
        max_length=15,
        unique=True,
    )
    full_name = models.CharField(
        _("full name"),
        max_length=100,
    )
    start_date = models.DateTimeField(
        _("start date"),
        default=timezone.now,
    )
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
    )

    objects = CustomAccountManager()
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", "full_name"]

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
