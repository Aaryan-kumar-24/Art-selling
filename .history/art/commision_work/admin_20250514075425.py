
from django.contrib import admin
from commision_work.models import Commision

class uploadAdmin(admin.ModelAdmin):
    display =("title" ,
"discription",
"art",
"price",)
# Register your models here.
admin.site.register(Upload,uploadAdmin)