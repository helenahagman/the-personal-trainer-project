from django import forms
from django.contrib.auth.models import User
from django.db import models
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


class AddBooking(forms.ModelForm):
    class Meta:
        model = BookingSession
        fields = (
            'name',
            'email',
            'age',  # Include 'age' field in the form
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
