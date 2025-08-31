from django.contrib import admin
from .models import Commission

class CommissionAdmin(admin.ModelAdmin):
    list_display = (
        "email",
        "phone",
        "medium",
        "price",
        "is_booked",
        "image"
"customization"

    )
    
admin.site.register(Commission, CommissionAdmin)
