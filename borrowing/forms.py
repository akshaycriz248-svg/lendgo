# borrowing/forms.py

from django import forms
from .models import BorrowRequest
from datetime import date


class BorrowRequestForm(forms.ModelForm):
    # Define fields explicitly to use DateInput widget
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'min': date.today}), label="Start Date")
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'min': date.today}), label="End Date")

    class Meta:
        model = BorrowRequest
        fields = ['start_date', 'end_date']

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("start_date")
        end_date = cleaned_data.get("end_date")

        if start_date and end_date:
            if start_date < date.today():
                raise forms.ValidationError("Start date cannot be in the past.")
            if end_date <= start_date:
                raise forms.ValidationError("End date must be after the start date.")

        return cleaned_data