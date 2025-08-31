
# Register your models here.
from django.contrib import admin
from artist.models import Artist

class artistAdmin(admin.ModelAdmin):
    list_display =("artistpic" ,
"artistname",)
# Register your models here.
admin.site.register(Artist,artistAdmin)