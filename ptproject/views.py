from django.contrib.auth import login, authenticate, get_user_model
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import generic, View
from django.views.generic.edit import CreateView
from django.views.generic import FormView
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils import timezone
from django.contrib import messages
from .models import BookingRequest, Contact, UserProfile
from .forms import BookingRequestForm, ContactForm, RegistrationForm


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


def register(request):
    """
    To render the registration view.
    """
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = RegistrationForm()
    
    context = {
        'title': 'Register',
        'form': form,
    }
    return render(request, 'register.html', context)


def log_in(request):
    """
    To render the login in view.
    """
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    
    context = {
        'title': 'Login',
        'form' : form,
    }
    return render(request, 'login.html', context)


class ContactView(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = "contact.html"
    success_url = reverse_lazy("contact_success")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Contact"
        return context


def book_request_view(request):
    if request.method == 'POST':
        form = BookingRequestForm(request.POST)
        if form.is_valid():
            booking_request = form.save(commit=False)
            booking_request.save()
            return redirect('success_page')
    else:
        form = BookingRequestForm()

    return render(request, 'book.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form. is_valid():
            user = form.save()
            # Log in the user efter registration
            login(request, user)
            return redirect('success_page')
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})


def log_in(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('success_page')
        else:
            # Handle invalid login credentials
            messages.error(
                request, 'Invalid email or password. Please try again.')
            return render(request, 'login.html')

    return render(request, 'login.html')


def home_view(request):
    return render(request, 'index.html')


class MyBookings(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        user = request.user
        current_time = timezone.now()

        future_bookings = BookingRequest.objects.filter(
            username=user, date__gt=current_time
        ).order_by("date")
        past_bookings = BookingRequest.objects.filter(
            username=user, date__lte=current_time
        ).order_by("-date")
        return render(
            request,
            "my_bookings.html",
            {
                "future_bookings": future_bookings,
                "past_bookings": past_bookings,
                "page_title": "My Bookings",
            },
        )

    def post(self, request, *args, **kwargs):
        booking_id = request.POST.get("booking_id")
        if booking_id:
            booking = BookingRequest.objects.filter(id=booking_id).first()

            if booking and booking.username == request.user:
                # Cancel booking
                booking.delete()
                messages.success(request, "Booking canceled successfully.")
            else:
                messages.error(request, "Unable to cancel the booking.")

        return HttpResponseRedirect(reverse("my_bookings"))


class SessionDetail(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = BookingRequest.objects.filter(approved=True)
        session = get_object_or_404(queryset, slug=slug)
        trainer = session.trainer
        user = get_user_model()
        has_booking = False

        booking_form = BookingRequestForm()

        if user.is_authenticated:
            has_booking = self.user_has_booked(user, session)

        return render(
            request,
            "session_detail.html",
            {
                "session": session,
                "trainer": trainer,
                "has_booking": has_booking,
                "booking_form": booking_form,
                "page_title": session.title,
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = BookingRequest.objects.filter(approved=True)
        session = get_object_or_404(queryset, slug=slug)
        trainer = session.trainer
        booking_form = BookingRequestForm()
        user = get_user_model()
        submitted_booking = False

        if user.is_authenticated:
            has_booking = self.user_has_booked(user, session)
            if has_booking:
                # User has already made a booking, return an error response
                messages.error(
                    request,
                    "You have already requested a personal training session!"
                    "Please check My Bookings page.",
                )
            else:
                if "booking_submit" in request.POST:
                    booking_form = BookingRequestForm(data=request.POST)
                    if booking_form.is_valid():
                        booking = booking_form.save(commit=False)
                        booking.session = session
                        booking.username = user
                        booking.save()
                        submitted_booking = True
                        messages.success(
                            request, "Thank you for your booking request!")
                    else:
                        booking_form = BookingRequestForm()

        return render(
            request,
            "session_detail.html",
            {
                "session": session,
                "trainer": trainer,
                "submitted_booking": submitted_booking,
                "booking_form": booking_form,
                "page_title": session.title,
            },
        )

    def user_has_booked(self, user, session):
        return BookingRequest.objects.filter(
            session=session,
            username=user
            ).exists()
