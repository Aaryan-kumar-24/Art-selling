from django.contrib import admin

# Register your models here.

from learn.models import Learn

class learnAdmin(admin.ModelAdmin):
    list_display =("title" ,

"discription",
"vedio",
)
# Register your models here.
admin.site.register(Learn,learnAdmin)