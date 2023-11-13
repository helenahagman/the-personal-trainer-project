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

    class YourForm(forms.Form):
        name = forms.CharField(label='Name', max_length=100)
        phonenumber = forms.CharField(label='Phone Number', max_length=15)
        email = forms.EmailField(label='Email')
        age = forms.IntegerField(label='Age')
        gender = forms.ChoiceField(label='Gender', choices=[(
            'male', 'Male'), ('female', 'Female'), ('other', 'Other')])
        message = forms.CharField(label='Message', widget=forms.Textarea)
        date = forms.DateField(label='Date')
        time = forms.TimeField(label='Time')


class ContactForm(forms.ModelForm):
    """
    A form for contact

    """

    class Meta:
        model = Contact
        fields = ('name', 'email', 'contact_message')
