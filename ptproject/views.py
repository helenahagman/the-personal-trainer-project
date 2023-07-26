from django.shortcuts import render, redirect
from django.views import generic
from .models import BookingForm


class BookingSession(models.Model):
    template_name = 'book.html'
    date = models.DateField()
    time = models.TimeField()
