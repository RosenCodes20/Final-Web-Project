from django.contrib.auth import get_user_model
from django.db import models


UserModel = get_user_model()

class Event(models.Model):

    team_versus = models.CharField(
        max_length=200
    )

    date = models.DateField()

    time = models.TimeField()

    location = models.CharField(
        max_length=150
    )

    is_training = models.BooleanField(
        default=False,
        null=True,
        blank=True
    )

    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE
    )


class EventAttendance(models.Model):
    attended = models.BooleanField(
        default=False
    )

    timestamp = models.DateTimeField(
        auto_now_add=True
    )

    event = models.ForeignKey(
        to=Event,
        on_delete=models.CASCADE
    )

    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE
    )