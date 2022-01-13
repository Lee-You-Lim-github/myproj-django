from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator


class TimestampedModel(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Spot(TimestampedModel):
    destination = models.CharField(max_length=200, db_index=True)
    area = models.CharField(max_length=100)
    content = models.TextField(validators=[
        MinLengthValidator(10)
    ])
    photo = models.ImageField(blank=True)

