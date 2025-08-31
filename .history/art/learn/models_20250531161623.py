from django.db import models



# Create your models here.
class Learn(models.Model):
    artist = models.TextField()
    title = models.TextField()
    discription = models.TextField()
    vedio = models.FileField(upload_to='static/')