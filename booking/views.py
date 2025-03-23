from django.shortcuts import render
from .models import Trainer, Class, Booking

def home(request):
    trainers = Trainer.objects.all()
    classes = Class.objects.all()
    bookings = Booking.objects.all()
    context = {
        'trainers': trainers,
        'classes': classes,
        'bookings': bookings,
    }
    return render(request, 'booking/home.html', context)
