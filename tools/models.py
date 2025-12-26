# tools/models.py

from django.db import models
from users.models import CustomUser


# You might need to import ToolForm here if it's a Tool-specific form
# from .forms import ToolForm

class Category(models.Model):
    """Model to define tool categories."""
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)  # Optional, but good practice for URLs

    class Meta:
        verbose_name_plural = "Categories"  # Fixes "Categorys" in Admin

    def __str__(self):
        return self.name


class Tool(models.Model):
    """Model for a lendable tool."""
    DISTRICTS = [
        ('Kollam', 'Kollam'),
        ('Thiruvananthapuram', 'Thiruvananthapuram'),
        ('Ernakulam', 'Ernakulam'),
        ('Thrissur', 'Thrissur'),
        ('Kozhikode', 'Kozhikode'),
        ('Malappuram', 'Malappuram'),
        ('Palakkad', 'Palakkad'),
        ('Alappuzha', 'Alappuzha'),
        ('Kottayam', 'Kottayam'),
        ('Idukki', 'Idukki'),
        ('Kannur', 'Kannur'),
        ('Wayanad', 'Wayanad'),
        ('Kasargod', 'Kasargod'),
        ('Pathanamthitta', 'Pathanamthitta'),
    ]

    owner = models.ForeignKey(CustomUser, related_name='tools', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='tools')
    name = models.CharField(max_length=255)
    description = models.TextField()
    daily_fee = models.DecimalField(max_digits=6, decimal_places=2)
    condition = models.CharField(max_length=50)
    image = models.ImageField(upload_to='tools/', blank=True, null=True)
    phone = models.CharField(max_length=15)

    district = models.CharField(
        max_length=30,
        choices=DISTRICTS
    )

    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Field added in the previous step
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # ... (other methods)