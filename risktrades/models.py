from django.db import models
from django.conf import settings
import os
from django.utils import timezone

# Function for trade image upload path
def risktrade_image_path(instance, filename):
    return os.path.join('risktrades', instance.currency_pair, filename)

# Updated model name: RiskTrade
class RiskTrade(models.Model):
    currency_pair = models.CharField(max_length=50)  # Currency pair (text input)
    risk_pips = models.IntegerField()  # Risk in pips
    risk_dollars = models.DecimalField(max_digits=10, decimal_places=2)  # Risk in USD
    risk_tsh = models.DecimalField(max_digits=15, decimal_places=2)  # Risk in TZS
    gain_pips = models.IntegerField()  # Gain in pips
    gain_dollars = models.DecimalField(max_digits=10, decimal_places=2)  # Gain in USD
    gain_tsh = models.DecimalField(max_digits=15, decimal_places=2)  # Gain in TZS
    mt5_chart = models.ImageField(upload_to=risktrade_image_path, blank=True, null=True)  # MT5 chart image
    tradeview_chart = models.ImageField(upload_to=risktrade_image_path, blank=True, null=True)  # TradeView chart image
    mt5_positions = models.ImageField(upload_to=risktrade_image_path, blank=True, null=True)  # MT5 Positions image
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='risktrades')  # Trader/user
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for creation
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp for updates
    
    # New fields for date and day name
    date = models.CharField(max_length=20, blank=True, null=True)  # Store the formatted date
    day_name = models.CharField(max_length=20, blank=True, null=True)  # Store the name of the day

    def save(self, *args, **kwargs):
        # Use timezone.now() if created_at is None
        created_date = self.created_at or timezone.now()

        self.date = created_date.strftime("%dth %b %Y")  # Format: 13th Feb 2025
        self.day_name = created_date.strftime("%A")  # Format: Tuesday

        super().save(*args, **kwargs)


    def __str__(self):
        return f"{self.currency_pair} - Risk: {self.risk_pips} pips, Gain: {self.gain_pips} pips"
