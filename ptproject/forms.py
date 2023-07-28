from django import forms
from .models import BookingSession, UserProfile


class BookingForm(forms.ModelForm):
    class Meta:
        model = BookingSession
        fields = ['date', 'time']

    def clean_date(self):
        """
        Past date should not be bookable
        """
        date = self.cleaned_date.get('date')

        if date:
            current_date = timezone.now().date()
            if date < current_date:
                raise forms.ValidationError(
                    "Selected date needs to be a future date")
            return date


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }
