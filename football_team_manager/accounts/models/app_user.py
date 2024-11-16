from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from football_team_manager.accounts.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(
        unique=True,
        null=False,
        blank=False
    )

    is_staff = models.BooleanField(
        default=False
    )

    is_active = models.BooleanField(
        default=True
    )

    USERNAME_FIELD = "email"

    objects = UserManager()