from django import forms
from django.core.validators import MinValueValidator
from django.utils import timezone
from .models import Booking, Contact

from django.contrib.auth import get_user_model
User = get_user_model()


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'


class BookingForm(forms.ModelForm):
    """
    A form for booking sessions.

    """

    class Meta:
        model = Booking
        fields = ('places_reserved',)


class ContactForm(forms.ModelForm):
    """
    A form for contact

    """

    class Meta:
        model = Contact
        fields = ('name', 'email', 'contact_message')
