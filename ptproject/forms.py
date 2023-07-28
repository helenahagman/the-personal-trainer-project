from django import forms
from .models import BookingSession, UserProfile


class BookingForm(forms.ModelForm):
    class Meta:
        model = BookingSession
        fields = ['date', 'time']


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }
