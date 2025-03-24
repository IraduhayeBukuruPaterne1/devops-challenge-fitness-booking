from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Booking
from .forms import BookingForm

# Home view to redirect to booking list
def home(request):
    return redirect('booking_list')  # Redirect to the list of bookings

def book_class(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.booking_date = timezone.now()
            booking.save()
            return redirect('booking_success')
    else:
        form = BookingForm()
    return render(request, 'booking_form.html', {'form': form})

def booking_success(request):
    return render(request, 'booking_success.html')

def booking_list(request):
    bookings = Booking.objects.all()
    return render(request, 'booking_list.html', {'bookings': bookings})

def booking_detail(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    return render(request, 'booking_detail.html', {'booking': booking})

