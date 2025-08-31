from django.contrib import admin

# Register your models here.

from learn.models import Learn

class uploadAdmin(admin.ModelAdmin):
    display =("title" ,
"discription",
"artist",
"medium",)
# Register your models here.
admin.site.register(Learn,uploadAdmin)