from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from django.contrib.auth.decorators import login_required
from .forms import BookingForm, RegistrationForm
from .models import BookingSession


class Home(generic.TemplateView):
    # Opens start page
    template_name = "index.html"


class PersonalTrainer(generic.TemplateView):
    # Opens personal trainer page
    template_name = "personaltrainer.html"


class Member(generic.TemplateView):
    # Opens member page
    template_name = "member.html"


class Book(generic.TemplateView):
    # Opens book page
    template_name = "book.html"


class Profile(generic.TemplateView):
    # Opens profile page
    template_name = "profile.html"


class Register(generic.TemplateView):
    # Opens register page
    template_name = "register.html"


# class BookingForm(forms.ModelForm):
#    class Meta:
#        model = BookingSession
#        fields = ['name', 'email', 'date', 'time']


def book_session(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to success page
            return redirect('success')
    else:
        form = BookingForm()

    return render(request, 'book.html', {'form': form})


@login_required
def profile_view(request):
    return render(request, 'profile.html')


def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to the profile page after successful registration
            return redirect('profile')
    else:
        form = RegistrationForm()

    return render(request, 'register_template.html', {'form': form})
