from django.contrib import admin

# Register your models here.

from learn.models import Learn

class learnAdmin(admin.ModelAdmin):
    display =("title" ,
"discription",
"vedio",
"artist",
)
# Register your models here.
admin.site.register(Learn,uploadAdmin)