from django.contrib import admin
from django import forms
from .models import BookingSession
from .views import BookingForm


class BookingSessionAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'date', 'time']
    search_fields = ['name', 'email', 'date']
    actions = ['approve_bookings']


def approve_bookings(self, request, queryset):
    queryset.update(apporved=True)
