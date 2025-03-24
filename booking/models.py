from django.contrib.auth.models import User
from django.db import models

class Trainer(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)  # You can customize this field as needed

    def __str__(self):
        return self.name

class Class(models.Model):
    title = models.CharField(max_length=200)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    date = models.DateTimeField()

    def __str__(self):
        return self.title

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    user_name = models.CharField(max_length=100, blank=True)  # Optional for guest users
    user_email = models.EmailField(blank=True)  # Optional for guest users
    fitness_class = models.ForeignKey(Class, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.user:
            return f"Booking by {self.user.username} - {self.fitness_class.title}"
        return f"Guest booking by {self.user_name} - {self.fitness_class.title}"
