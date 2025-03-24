from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin panel URL
    path('', include('booking.urls')),  # Booking app URLs
]
