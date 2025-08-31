from django.contrib import admin
from .models import Feedback

class FeedbackAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'phone',
        'state',
        'city',
        'address',
        'checked',
    )
    search_fields = ('email', 'phone', 'state', 'city')
    list_filter = ('state', 'city', 'checked')

admin.site.register(Feedback, FeedbackAdmin)
