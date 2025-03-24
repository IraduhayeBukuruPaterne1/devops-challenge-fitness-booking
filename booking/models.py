from django.contrib.auth.models import User
from django.db import models

class Booking(models.Model):
    # Link booking to a Django user (if using authentication)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    user_name = models.CharField(max_length=100, blank=True)  # Optional for guest users
    user_email = models.EmailField(blank=True)  # Optional for guest users
    fitness_class = models.ForeignKey('Class', on_delete=models.CASCADE)  # Assuming Class model is defined elsewhere
    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Display user or name in the string representation
        if self.user:
            return f"Booking by {self.user.username} - {self.fitness_class.title}"
        return f"Guest booking by {self.user_name} - {self.fitness_class.title}"
