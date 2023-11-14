from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))


class BookingRequest(models.Model):
    name = models.CharField(max_length=100, default='State your name')
    phonenumber = models.CharField(max_length=15, default='1234567890')
    email = models.EmailField(max_length=70, default='your@mail.com')
    age = models.IntegerField(default='0', validators=[MinValueValidator(0)])
    gender = models.CharField(
        max_length=10,
        choices=[
            ('male', 'Male'),
            ('female', 'Female'),
            ('other', 'Other')
        ],
        default='male'
    )
    message = models.TextField(max_length=300, default='')
    date = models.DateField()
    time = models.TimeField()
    approved = models.BooleanField(default=False)
    objects = models.Manager()


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
    email = models.EmailField(unique=True, default='default@example.com')

    def __str__(self):
        if self.user and hasattr(self.user, 'username'):
            return self.user.username
        else:
            return f"UserProfile without associated User ({self.pk})"
