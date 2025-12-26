# reviews/models.py

from django.db import models
from django.contrib.auth import get_user_model
from borrowing.models import BorrowRequest

User = get_user_model()


class Review(models.Model):
    RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]  # 1 to 5 star rating

    # Who is reviewing whom/what
    borrow_request = models.ForeignKey(
        BorrowRequest,
        on_delete=models.CASCADE,
        related_name='reviews'
    )

    # Who wrote the review
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='submitted_reviews')

    # Rating for the Tool/Owner/Borrower
    rating = models.IntegerField(choices=RATING_CHOICES)
    comment = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    # Type of review (e.g., Tool Review, Borrower Review)
    review_type = models.CharField(max_length=50, choices=[
        ('TOOL', 'Review of Tool'),
        ('BORROWER', 'Review of Borrower (by Owner)'),
        ('OWNER', 'Review of Owner (by Borrower)'),
    ])

    def __str__(self):
        return f"{self.review_type} for {self.borrow_request.tool.name} - {self.rating} stars"