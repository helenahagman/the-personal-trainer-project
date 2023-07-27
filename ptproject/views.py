from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from .models import BookingForm


class Home(generic.TemplateView):
    #Opens start page
    template_name = "index.html"


class pt(generic.TemplateView):
    # Opens personal trainer page
    template_name = "pt.html"


class Member(generic.TemplateView):
    # Opens member page
    template_name = "member.html"


class BookingSession(models.Model):
    model = BookingForm
    template_name = 'book.html'
    date = models.DateField()
    time = models.TimeField()
