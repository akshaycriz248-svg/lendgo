# tools/admin.py

from django.contrib import admin
from .models import Category, Tool

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Tool)
class ToolAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'category', 'condition', 'daily_fee', 'is_available')
    list_filter = ('is_available', 'category', 'condition', 'owner',)
    search_fields = ('name', 'description','phone','district',)
    actions = ['mark_available', 'mark_unavailable']

    @admin.action(description='Mark selected tools as Available')
    def mark_available(self, request, queryset):
        queryset.update(is_available=True)

    @admin.action(description='Mark selected tools as Unavailable')
    def mark_unavailable(self, request, queryset):
        queryset.update(is_available=False)