from django.db import models

# Create your models here.
class Day01(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
