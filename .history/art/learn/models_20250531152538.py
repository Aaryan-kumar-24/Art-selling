from django.db import models



# Create your models here.
class Learn(models.Model):
    title = models.TextField()
    discription = models.TextField()
    artist = models.ImageField(upload_to='static/')
    artsit = models.IntegerField()