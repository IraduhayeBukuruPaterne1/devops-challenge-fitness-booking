from django.shortcuts import render, redirect
from .forms import BookingForm

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

