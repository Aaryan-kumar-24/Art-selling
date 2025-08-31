from django.db import models



# Create your models here.
class L(models.Model):
    title = models.TextField()
    discription = models.TextField()
    art = models.ImageField(upload_to='static/')
    price = models.IntegerField()