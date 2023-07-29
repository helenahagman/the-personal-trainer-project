from django import forms
from django.core.validators import MinValueValidator
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .models import BookingSession

User = get_user_model()


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'


class AddBooking(forms.ModelForm):
    class Meta:
        model = BookingSession
        fields = (
            'name',
            'email',
            'age',
            'date',
            'time',
        )

        widgets = {
            'date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'class': 'form-control',
                    'type': 'date'
                }
            ),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }

    def clean_date(self):
        """
        Past date should not be bookable
        """
        date = self.cleaned_data.get('date')

        if date:
            current_date = timezone.now().date()
            if date < current_date:
                raise forms.ValidationError("Date needs to be a future date")

        return date

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date'].widget.attrs.update({'class': 'form-control'})
