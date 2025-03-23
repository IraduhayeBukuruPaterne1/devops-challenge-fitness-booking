from django.contrib import admin
from .models import Trainer, Class, Booking

@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialization')
    search_fields = ('name', 'specialization')

@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ('title', 'trainer', 'date')
    search_fields = ('title', 'trainer__name')
    list_filter = ('date', 'trainer')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'user_email', 'fitness_class', 'booking_date')
    search_fields = ('user_name', 'user_email', 'fitness_class__title')
    list_filter = ('booking_date',)
