from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.book_class, name='book_class'),
    path('success/', views.booking_success, name='booking_success'),
]

