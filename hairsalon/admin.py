from django.contrib import admin
from .models import Salon, SalonStaff, News


class SalonAdmin(admin.ModelAdmin):
    fields = ['uuid', 'name', 'phone_number', 'address', 'created_at', 'updated_at',]
    readonly_fields = ('uuid', 'created_at', 'updated_at',)
    list_display = ('uuid', 'name', 'phone_number', 'address', 'created_at', 'updated_at',)

# Register your models here.

admin.site.register(News)
admin.site.register(SalonStaff)
admin.site.register(Salon, SalonAdmin)