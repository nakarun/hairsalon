from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import BaseUser, SalonStaff, CustomerUser

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.utils.translation import ugettext_lazy as _


class SalonStaffChangeForm(UserChangeForm):
    class Meta:
        model = SalonStaff
        fields = '__all__'


class CustomerUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomerUser
        fields = '__all__'


class SalonStaffCreationForm(UserCreationForm):
    class Meta:
        model = SalonStaff
        fields = ("username", "salon",)


class CustomerUserCreationFOrm(UserCreationForm):
    class Meta:
        model = CustomerUser
        fields = ("username",)


class SalonStaffAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (_('Salon data'), {'fields': ('salon', 'is_owner', 'image', 'message', )}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'salon'),
        }),
    )
    form = UserChangeForm
    add_form = SalonStaffCreationForm
    list_display = ('username', 'salon', 'email', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('username', 'first_name', 'last_name', 'email')


# Register your models here.
admin.site.register(BaseUser, UserAdmin)
admin.site.register(SalonStaff, SalonStaffAdmin)
admin.site.register(CustomerUser, UserAdmin)