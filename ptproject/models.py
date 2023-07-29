from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator


class BookingSession(models.Model):
    name = models.CharField(max_length=80, default='Name', blank=False)
    email = models.EmailField(default='example@example.com', blank=False)
    age = models.CharField(max_length=2, default='18', blank=False)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(unique=True, blank=False)
    password = models.CharField(max_length=128, blank=False)
