from django.db import models
from django.conf import settings
import os

# Function for game image upload path
def game_image_path(instance, filename):
    # Upload image to games/<category>/<filename>
    return os.path.join('games', instance.category, filename)

# Game model
class Game(models.Model):
    CATEGORY_CHOICES = [
        ('Educational', 'Educational'),
        ('Action', 'Action'),
        ('Puzzle', 'Puzzle'),
        ('Adventure', 'Adventure'),
        ('For Fun', 'For Fun'),
        ('Creative', 'Creative'),
        ('Other', 'Other'),
    ]

    name = models.CharField(max_length=200)  # Game title
    description = models.TextField(blank=True, null=True)  # Game description
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Game price
    stock = models.PositiveIntegerField()  # Available stock
    sold = models.PositiveIntegerField(default=0)  # Units sold
    rating = models.PositiveSmallIntegerField(default=0)  # Customer rating
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Other')  # Game category
    image = models.ImageField(upload_to=game_image_path, blank=True, null=True)  # Game cover image
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='games')  # Seller/creator of the game
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for creation
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp for updates

    def remaining_stock(self):
        return self.stock - self.sold

    def __str__(self):
        return self.name
