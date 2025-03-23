from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Fitness Booking App!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # This line maps the home view to the root URL
]
