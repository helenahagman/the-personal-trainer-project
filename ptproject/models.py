from django.db import models
from django.contrib.auth.models import User

# returns a string representation of an object


class BookingSession(models.Model):
    date = models.DateField()
    time = models.TimeField()


def __str__(self):
    return self.title
