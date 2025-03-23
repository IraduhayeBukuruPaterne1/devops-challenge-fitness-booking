from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

# View functions
def home(request):
    return HttpResponse("Welcome to the Fitness Booking App!")

def about(request):
    return HttpResponse("This is the About page.")

# URL routing
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Home page
    path('about/', about, name='about'),  # About page
]
