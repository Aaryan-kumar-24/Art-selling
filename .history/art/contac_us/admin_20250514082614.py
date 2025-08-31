from django.contrib import admin
from .models import Feedback

class Admin(admin.ModelAdmin):
    list_display = (
        'email',
        'phone',
        'state',
        'city',
        'address',
        'checked',
    )
admin.site.register(Feedback, FeedbackAdmin)
