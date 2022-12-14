from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=30)
    summary = models.TextField()
    running_time = models.IntegerField(validators=[MinValueValidator(0)])
