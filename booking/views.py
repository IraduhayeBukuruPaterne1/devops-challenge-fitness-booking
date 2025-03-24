from django.shortcuts import render, redirect, get_object_or_404
from .forms import BookingForm
from .models import Booking

def book_class(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking_success')
    else:
        form = BookingForm()
    return render(request, 'booking/book_class.html', {'form': form})

def booking_success(request):
    return render(request, 'booking/booking_success.html')

def booking_list(request):
    bookings = Booking.objects.all()
    return render(request, 'booking/booking_list.html', {'bookings': bookings})

def booking_detail(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    return render(request, 'booking/booking_detail.html', {'booking': booking})
