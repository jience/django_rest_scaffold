from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from guardian.admin import GuardedModelAdmin

from .models import User


@admin.register(User)
class UserAdmin(UserAdmin, GuardedModelAdmin):
    list_display = ('username', 'email', 'date_joined', 'is_staff', 'updated_at')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {
            'fields': ('first_name', 'last_name', 'email', 'phone', 'company', 'dept', 'job')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
