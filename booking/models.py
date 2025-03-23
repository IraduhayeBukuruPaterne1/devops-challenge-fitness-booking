from django.db import models

class Trainer(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    specialization = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Class(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    date = models.DateTimeField()

    def __str__(self):
        return self.title


class Booking(models.Model):
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField()
    fitness_class = models.ForeignKey(Class, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_name} - {self.fitness_class.title}"
