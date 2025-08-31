from django.db import models

# Create your models here.
class Artist(models.Model):
    artistpic= models.ImageField(upload_to='static/',null=True)
    artistname= models.TextField(null="true")
