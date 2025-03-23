from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

# Define a simple view for the home page
def home(request):
    return HttpResponse("Welcome to the Fitness Booking App!")

urlpatterns = [
    # Admin interface URL
    path('admin/', admin.site.urls),
    
    # Root URL for the home page
    path('', home, name='home'),
]
