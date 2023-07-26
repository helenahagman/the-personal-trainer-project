from django.shortcuts import render, redirect
from .models import BookingForm


def book_session request:
    if request.method == 'POST'
    form = BookingForm('request.POST')
    if form.is_valid():
        form.save()
        # Redirect to success page
        return redirect('success_page')
    else:
        form = BookingForm()
    return render(request, 'booking_form.html', {'form': form})
