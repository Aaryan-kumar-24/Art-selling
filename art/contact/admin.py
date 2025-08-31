from django.contrib import admin
from .models import Contact

class contactAdmin(admin.ModelAdmin):
    list_display = (
'phonenumber',
'emailid',
'state',
'city',
'address',
'review',
    )
admin.site.register(Contact,contactAdmin)
