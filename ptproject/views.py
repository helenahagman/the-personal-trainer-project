from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from django.views.generic import FormView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .forms import AddBooking, RegistrationForm
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


class ProfileView(generic.TemplateView):
    # Opens profile page
    template_name = "profile.html"

    @login_required
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class Register(generic.TemplateView):
    # Opens register page
    template_name = "register.html"


class Login(generic.TemplateView):
    # Opens login page
    template_name = "login.html"


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


class RegisterView(FormView):
    template_name = "register.html"
    form_class = RegistrationForm
    # Redirect to a success page after successful registration
    success_url = reverse_lazy('registration_success')

    def form_valid(self, form):
        # Save the user profile to the database
        form.save()

        # Display the success message in the same template
        context = self.get_context_data(form=form)
        context['success_message'] = "Registration successful! You can now log in."
        return render(self.request, self.template_name, context)


def log_in(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('success_page')
        else:
            # Handle invalid login credentials (display error message, etc.)

            return render(request, 'login.html')
