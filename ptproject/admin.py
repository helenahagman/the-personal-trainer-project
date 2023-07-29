from django.contrib import admin
from django import forms
from .models import BookingSession


@admin.register(BookingSession)
class BookingSessionAdmin(admin.ModelAdmin):

    list_display = (
        'name', 'email', 'date', 'time'
    )
    search_fields = ['name', 'email', 'date', 'time']
    list_filter = ('name', 'email', 'date', 'time')
    actions = ['approve_bookings']

    def approve_bookings(self, request, queryset):
        queryset.update(apporved=True)
