from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class TradeReasons(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    currency_pair = models.CharField(max_length=6, null=True, blank=True)
    traders_idea_name = models.CharField(max_length=15, null=True, blank=True)
    trade_signal = models.CharField(max_length=5, choices=(("BUYS", "BUYS"), ("SELLS", "SELLS")), null=True, blank=True)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    # Hour and custom candles
    idea_candle = models.ImageField(upload_to='idea_candles/', null=True, blank=True)
    idea_candle_two = models.ImageField(upload_to='idea_candle_two/', null=True, blank=True)
    youtube_candle = models.ImageField(upload_to='youtube/', null=True, blank=True)
    volumetic_rejection_candle = models.ImageField(upload_to='volumetic_rejection_candles/', null=True, blank=True)
    fibonnaci_candle = models.ImageField(upload_to='fibonnaci_candles/', null=True, blank=True)
    ICT_killzone_candle = models.ImageField(upload_to='ICT_killzone_candles/', null=True, blank=True)
    ichimoku_candle = models.ImageField(upload_to='ichimoku_candles/', null=True, blank=True)
    ema_cross_alert_candle = models.ImageField(upload_to='ema_cross_alert_candles/', null=True, blank=True)
    ICT_institutional_order_candle = models.ImageField(upload_to='ICT_institutional_order_candles/', null=True, blank=True)
    daily_high_low_candle = models.ImageField(upload_to='daily_high_low_candle/', null=True, blank=True)
    all_indicators_candle = models.ImageField(upload_to='all_indicators_candle/', null=True, blank=True)
    blog_trade_post_candle = models.ImageField(upload_to='blog_trade_post_candle/', null=True, blank=True)
    blog_mt5_post_candle = models.ImageField(upload_to='blog_mt5_post_candle/', null=True, blank=True)
    stoploss_candle = models.ImageField(upload_to='stoploss_candle/', null=True, blank=True)

    class Meta:
        verbose_name = "Trade reason"
        verbose_name_plural = "Trade reasons"
