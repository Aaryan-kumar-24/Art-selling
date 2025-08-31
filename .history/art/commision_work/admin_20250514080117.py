from django.contrib import admin
from commision_work.models import Commision

class CommisionAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "discription",
        "art",
        "price",
    )

# Register your models here.
admin.site.register(Commision, CommisionAdmin)
