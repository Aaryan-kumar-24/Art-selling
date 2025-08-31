from django.db import models

# Create your models here.
class Upload(models.Model):
    title = models.TextField()
    discription = models.TextField()
    art = models.ImageField(upload_to='static/')
    price = models.IntegerField()


    from django.contrib import admin
from .models import Commission

class CommissionAdmin(admin.ModelAdmin):
    list_display = (
        "email",
        "phone",
        "medium",
        "price",
        "is_booked",
    )
    search_fields = ("email", "phone", "medium")
    list_filter = ("medium", "is_booked")

admin.site.register(Commission, CommissionAdmin)
