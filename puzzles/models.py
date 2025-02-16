from django.db import models
from django.conf import settings

class Puzzle(models.Model):
    AGE_GROUP_CHOICES = [
        ('under_5', 'Under 5 years'),
        ('under_10', 'Under 10 years'),
        ('under_18', 'Under 18 years'),
        ('above_18', '18 years and above'),
    ]
    
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    sold = models.PositiveIntegerField(default=0,blank=True, null=True)
    pieces = models.PositiveIntegerField()
    image = models.ImageField(upload_to='puzzle_images/', blank=True, null=True)   
    age_group = models.CharField(max_length=20, choices=AGE_GROUP_CHOICES)
    rating = models.PositiveSmallIntegerField(default=0)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='puzzles')  # Added user relationship
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)  # Timestamp for creation
    updated_at = models.DateTimeField(auto_now=True , blank=True, null=True)  # Timestamp for updates

    def remaining_stock(self):
        return self.stock - self.sold

    def __str__(self):
        return self.name
