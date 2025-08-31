from django.db import models

class Feedback(models.Model):
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    feedback = models.TextField()
    checked = models.BooleanField(default=False)  # corresponds to the "Check me out" checkbox

    def __str__(self):
        return f"{self.email} - {self.city}, {self.state}"
