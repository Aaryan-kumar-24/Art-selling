from django.db import models

# Create your models here.
class CommissionRequest(models.Model):
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    medium = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to='commissions/')
    customization = models.TextField()
    is_booked = models.BooleanField(default=False)
