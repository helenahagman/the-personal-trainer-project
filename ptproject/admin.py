from django.contrib import admin
from .models import Booking, Contact


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """
    Admin class for the Booking model.
    """

    # Change 'get_session_title' to 'id'
    list_display = ('id', 'username', 'places_reserved', 'approved')
    list_display_links = ('username',)
    list_filter = ('username', 'approved')  
    search_fields = ('username__username', 'approved')

    actions = ['approve_booking', 'unapprove_booking']

    def approve_booking(self, request, queryset):
        """
        Admin to approve booking requests.
        """

        queryset.update(approved='approved')

    def unapprove_booking(self, request, queryset):
        """
        Admin to deny booking requests.
        """

        queryset.update(approved='not_approved')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """
    Admin for Contact model.
    """

    list_display = ('name', 'email', 'contact_message', 'created_on')
    list_filter = ('name', 'email', 'created_on')
    list_display_links = ('name',)
    search_fields = ['name', 'email', 'contact_message', 'created_on']
