from django.db import models

# Create your models here.
class Upload(models.Model):
    title = models.TextField()
    discription = models.TextField()
    artwork