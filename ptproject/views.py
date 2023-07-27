from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from django import forms
from .forms import BookingForm
from .models import BookingSession


class Home(generic.TemplateView):
    # Opens start page
    template_name = "index.html"


class pt(generic.TemplateView):
    # Opens personal trainer page
    template_name = "pt.html"


class Member(generic.TemplateView):
    # Opens member page
    template_name = "member.html"


class BookingForm(forms.ModelForm):
    class Meta:
        model = BookingSession
        fields = ['name', 'email', 'date', 'time']


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
