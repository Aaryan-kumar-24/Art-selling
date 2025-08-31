from django.contrib import admin

# Register your models here.

from learn.models import Upload

class uploadAdmin(admin.ModelAdmin):
    display =("title" ,
"discription",
"art",
"price",)
# Register your models here.
admin.site.register(Upload,uploadAdmin)