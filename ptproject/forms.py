from django import forms
from django.core.validators import MinValueValidator
from django.utils import timezone
from .models import BookingSession, UserProfile


class BookingForm(forms.ModelForm):
    class Meta:
        model = BookingSession
        fields = ['date', 'time']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date'].widget.attrs.update({'class': 'form-control'})


    def clean_date(self):
        """
        Past date should not be bookable
        """
        date = self.cleaned_date.get('date')

        if date:
            current_date = timezone.now().date()
            if date < current_date:
                raise forms.ValidationError(
                    "Date needs to be a future date")
            return date


class RegisterForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }
