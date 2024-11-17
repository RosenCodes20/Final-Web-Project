from django.db import models


class SchemeChoices(models.TextChoices):

    FOUR_THREE_THREE = "4-3-3", "4-3-3"
    THREE_FOUR_THREE = "3-4-3", "3-4-3"
    THREE_FIVE_TWO = "3-5-2", "3-5-2"
    FOUR_FOUR_TWO = "4-4-2", "4-4-2"