from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Homepage route
    path('book/', views.book_class, name='book_class'),
    path('success/', views.booking_success, name='booking_success'),
    path('bookings/', views.booking_list, name='booking_list'),
    path('bookings/<int:booking_id>/', views.booking_detail, name='booking_detail'),
]

