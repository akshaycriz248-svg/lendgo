# borrowing/admin.py

from django.contrib import admin
from .models import BorrowRequest

@admin.register(BorrowRequest)
class BorrowRequestAdmin(admin.ModelAdmin):
    list_display = ('tool', 'borrower', 'request_date', 'start_date', 'end_date', 'status')
    list_filter = ('status', 'request_date', 'tool__owner', 'borrower')
    search_fields = ('tool__name', 'borrower__username')
    readonly_fields = ('request_date',)