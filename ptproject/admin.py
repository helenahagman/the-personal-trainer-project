from django.contrib import admin
from django import forms
from .models import BookingSession


class BookingForm(forms.ModelForm):
    class Meta:
        model = BookingSession
        fields = ['date', 'time']
