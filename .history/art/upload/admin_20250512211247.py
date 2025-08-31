from django.contrib import admin
from upload.models import Upload

class uploadAdmin(admin.ModelAdmin):
    display =(title ,
discription,
art,
price,)
# Register your models here.
