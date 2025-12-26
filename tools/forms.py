# tools/forms.py

from django import forms
from .models import Tool, Category


class ToolForm(forms.ModelForm):
    """
    Form for creating and updating Tool listings.
    """

    class Meta:
        model = Tool
        # Specify the fields the user is allowed to edit
        fields = [
            'name',
            'description',
            'category',
            'condition',
            'daily_fee',
            'image',
            'phone',
            'district',
            'is_available'
        ]

        # Optional: Add custom labels and widgets for better UX
        labels = {
            'daily_fee': 'Daily Rental Fee (₹)',
            'is_available': 'Available for Rent',
        }

        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'daily_fee': forms.NumberInput(attrs={'step': '0.01'}),
        }