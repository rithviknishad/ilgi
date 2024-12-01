from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from utils.models import BaseModel


class EnergyLog(BaseModel):
    title = models.CharField(max_length=255)
    story = models.TextField()
    date = models.DateField()
    energy_delta = models.SmallIntegerField(
        validators=[MinValueValidator(-5), MaxValueValidator(5)]
    )
    created_by = models.ForeignKey(
        "users.User", on_delete=models.PROTECT, related_name="+"
    )
