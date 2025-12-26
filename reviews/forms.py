# reviews/forms.py

from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment', 'review_type']
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 3}),
            'review_type': forms.HiddenInput(), # Will be set programmatically
        }