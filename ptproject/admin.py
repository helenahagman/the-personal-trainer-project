from django.contrib import admin
from .models import BookingRequest, Contact


class ApprovedFilter(admin.SimpleListFilter):
    title = 'Approved'
    parameter_name = 'approved'

    def lookups(self, request, model_admin):
        return (
            ('approved', 'Approved'),
            ('not_approved', 'Not Approved'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'approved':
            return queryset.filter(approved=True)
        elif self.value() == 'not_approved':
            return queryset.filter(approved=False)


@admin.register(BookingRequest)
class BookingAdmin(admin.ModelAdmin):
    """
    Admin class for the Booking model.
    """

    list_display = ('id', 'name', 'phonenumber', 'email', 'age',
                    'gender', 'message', 'date', 'time', 'approved')
    search_fields = ('name', 'get_approved')
    list_filter = ('name', ApprovedFilter)

    actions = ['approve_booking', 'unapprove_booking']

    def get_approved(self, obj):
        """
        Admin to approve booking requests.
        """
        return obj.approved
    get_approved.short_description = 'Request Approved'

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
