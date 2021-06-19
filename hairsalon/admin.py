from django.contrib import admin
from .models import Salon, BaseUser, SalonStaff, News

# Register your models here.

admin.site.register(BaseUser)
admin.site.register(News)
admin.site.register(SalonStaff)
admin.site.register(Salon)