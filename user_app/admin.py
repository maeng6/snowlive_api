# user_app/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from user_app.models import CustomUser  # 정확한 경로를 지정

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['email', 'username', 'uid', 'is_staff', 'is_active']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('uid',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
