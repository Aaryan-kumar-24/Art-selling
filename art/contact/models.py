from django.db import models

class Contact(models.Model):
    phonenumber = models.CharField(max_length=15)
    emailid = models.EmailField()
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    review = models.TextField()