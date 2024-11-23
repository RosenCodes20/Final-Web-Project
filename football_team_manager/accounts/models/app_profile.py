from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(
        to=UserModel,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name="profile"
    )

    first_name = models.CharField(
        max_length=200,
        null=True,
        blank=True
    )

    last_name = models.CharField(
        max_length=200,
        null=True,
        blank=True
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True
    )

    profile_picture = models.URLField(
        null=True,
        blank=True
    )

    def get_profile_full_name(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"

        elif not self.first_name and not self.last_name:
            return "Anonymous User"

        return self.first_name if self.first_name else self.last_name