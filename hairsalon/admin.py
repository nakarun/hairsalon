from django.contrib import admin
from .models import Salon, SalonStaff, News

# Register your models here.

admin.site.register(News)
admin.site.register(SalonStaff)
admin.site.register(Salon)