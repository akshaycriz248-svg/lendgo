# borrowing/models.py

from django.db import models
from django.contrib.auth import get_user_model
from tools.models import Tool

User = get_user_model()


class BorrowRequest(models.Model):
    STATUS_CHOICES = [
        ('REQUESTED', 'Requested'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected'),
        ('ACTIVE', 'Active (Currently Borrowed)'),
        ('RETURNED', 'Returned (Waiting for Owner Check)'),
        ('CLOSED', 'Closed (Completed)'),
        ('CANCELED', 'Canceled'),
    ]

    tool = models.ForeignKey(Tool, on_delete=models.CASCADE, related_name='borrow_requests')
    borrower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='outgoing_requests')

    start_date = models.DateField()
    end_date = models.DateField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='REQUESTED'
    )

    request_date = models.DateTimeField(auto_now_add=True)
    # Link to Review (if one is created after closing)
    review = models.OneToOneField('reviews.Review', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.tool.name} requested by {self.borrower.username} ({self.status})"

    class Meta:
        # Ensures a borrower can't request the same tool for conflicting dates
        # (initial simple constraint)
        constraints = [
            models.UniqueConstraint(
                fields=['tool', 'borrower', 'status'],
                condition=~models.Q(status__in=['REJECTED', 'CLOSED', 'CANCELED']),
                name='unique_active_request'
            )
        ]