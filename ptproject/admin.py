from django.contrib import admin
from django import forms
from .models import BookingSession
from .views import BookingForm


class BookingSessionAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'date', 'time']


admin.site.register(BookingSession, BookingSessionAdmin)
