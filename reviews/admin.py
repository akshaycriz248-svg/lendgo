# reviews/admin.py

from django.contrib import admin
from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('borrow_request', 'reviewer', 'rating', 'review_type', 'created_at')
    list_filter = ('rating', 'review_type', 'created_at')
    search_fields = ('comment', 'reviewer__username')
    readonly_fields = ('created_at',)