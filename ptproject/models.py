from django.utils import timezone
from django import forms
from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MinValueValidator
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))


class Booking(models.Model):
    """
    Model for booking a session.
    """

    APPROVAL_CHOICES = (
        ('approved', 'Approved'),
        ('pending', 'Pending'),
        ('not_approved', 'Not Approved'),
    )

    username = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_bookings')
    places_reserved = models.IntegerField(validators=[MinValueValidator(1), ])
    approved = models.CharField(
        max_length=12, choices=APPROVAL_CHOICES, default='pending')

    def __str__(self):
        return f'{self.id} is booked by {self.username}'

class Contact(models.Model):
    """
    Model for contact messages.

    """

    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact_message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']
        verbose_name_plural = 'Contact Messages'

    def __str__(self):
        return f'Contact message submitted by {self.name} on {self.created_on}'


class UserProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'
