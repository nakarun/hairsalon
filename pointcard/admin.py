from django.contrib import admin

# Register your models here.
from pointcard.models import CustomerUser, PointCard, Stamp


class PointCardAdmin(admin.ModelAdmin):
    fields = ['uuid', 'salon', 'vertical_cells_count', 'horizontal_cells_count', 'created_at', 'updated_at']
    readonly_fields = ('uuid', 'created_at', 'updated_at',)
    list_display = ('uuid', 'salon', 'vertical_cells_count', 'horizontal_cells_count', 'created_at', 'updated_at')


admin.site.register(CustomerUser)
admin.site.register(PointCard, PointCardAdmin)
admin.site.register(Stamp)