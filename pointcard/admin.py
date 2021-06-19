from django.contrib import admin

# Register your models here.
from pointcard.models import CustomerUser, SalonPointCard, Appointment


class SalonPointCardAdmin(admin.ModelAdmin):
    fields = ['uuid', 'salon', 'max_stamp', 'created_at', 'updated_at']
    readonly_fields = ('uuid', 'created_at', 'updated_at',)
    list_display = ('uuid', 'salon', 'max_stamp', 'created_at', 'updated_at')


admin.site.register(CustomerUser)
admin.site.register(SalonPointCard, SalonPointCardAdmin)
admin.site.register(Appointment)