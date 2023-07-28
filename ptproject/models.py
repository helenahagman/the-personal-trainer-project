from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator


class BookingSession(models.Model):
    name = models.CharField(max_length=80, default='Name', blank=False)
    email = models.EmailField(default='example@example.com', blank=False)
    age = models.IntegerField(
        default='18',
        blank=False,
        validators=[
            MinValueValidator(18)
        ]
    )
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
