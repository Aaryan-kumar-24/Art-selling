from django.db import models



# Create your models here.
class Learn(models.Model):
    title = models.TextField()
    discription = models.TextField()
    vedio = models.(upload_to='static/')
    artsit = models.IntegerField()