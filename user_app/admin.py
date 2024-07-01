from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User  # User로 수정

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ['email', 'username', 'uid', 'is_staff', 'is_active']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('uid',)}),
    )

admin.site.register(User)
