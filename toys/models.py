from django.db import models
from django.conf import settings
import os

class Toy(models.Model):
    # Toy categories as choices
    CATEGORY_CHOICES = [
        ('Educational', 'Educational'),
        ('Action', 'Action'),
        ('Puzzle', 'Puzzle'),
        ('Plush', 'Plush'),
        ('For Fun', 'For Fun'),
        ('Creative', 'Creative'),
        ('Other', 'Other'),
    ]

    # Age group choices
    AGE_GROUP_CHOICES = [
        ('0-2 years', '0-2 years'),
        ('3-5 years', '3-5 years'),
        ('6-8 years', '6-8 years'),
        ('9+ years', '9+ years'),
    ]

    # Model fields
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    sold = models.PositiveIntegerField(default=0)
    pieces = models.PositiveIntegerField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Other')
    age_group = models.CharField(max_length=20, choices=AGE_GROUP_CHOICES, default='3-5 years')
    image = models.ImageField(upload_to='toy_images/', blank=True, null=True)
    rating = models.PositiveSmallIntegerField(default=0)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='toys')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)  # Timestamp for creation
    updated_at = models.DateTimeField(auto_now=True , blank=True, null=True)  # Timestamp for updates

    # Utility methods
    def remaining_stock(self):
        return self.stock - self.sold

    def __str__(self):
        return self.name
