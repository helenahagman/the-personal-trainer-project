from django import forms
from django.core.validators import MinValueValidator
from django.utils import timezone
from django.contrib.auth.forms import AuthenticationForm
from .models import BookingRequest, Contact, UserProfile

from django.contrib.auth import get_user_model


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }


class LoginForm(AuthenticationForm):

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password']


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'


class BookingRequestForm(forms.ModelForm):
    """
    Form for booking request
    """
    class Meta:
        model = BookingRequest
        fields = ['name', 'phonenumber', 'email',
                  'age', 'gender', 'message', 'date', 'time']

    widgets = {
        'date': forms.DateInput(attrs={'type': 'date'}),
        'time': forms.TimeInput(attrs={'type': 'time'}),
    }


class ContactForm(forms.ModelForm):
    """
    A form for contact

    """

    class Meta:
        model = Contact
        fields = ('name', 'email', 'contact_message')
