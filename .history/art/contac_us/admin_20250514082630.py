from django.contrib import admin
from .models import Contact

class contactAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'phone',
        'state',
        'city',
        'address',
        'checked',
    )
admin.site.register(Feedback, contactAdmin)
