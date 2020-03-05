from django.db import models
from django.utils import timezone

class Lead(models.Model):
    nickname = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.CharField(max_length=400)
    created_at = models.DateTimeField(default=timezone.now)
