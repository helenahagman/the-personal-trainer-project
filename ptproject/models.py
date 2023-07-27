from django.db import models
from django.contrib.auth.models import User


class BookingSession(models.Model):
    name = models.CharField(max_length=80, default='Name')
    email = models.EmailField(default='example@example.com')
    date = models.DateField()
    time = models.TimeField()


def __str__(self):
    return self.name
