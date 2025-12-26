# users/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Registering the CustomUser model with the CustomUserAdmin class
class CustomUserAdmin(UserAdmin):
    # Customize the fieldsets for the admin change form
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone_number', 'location')}),
    )
    # Customize the fields to display in the list view
    list_display = ('username', 'email', 'is_staff', 'phone_number', 'location')

admin.site.register(CustomUser, CustomUserAdmin)