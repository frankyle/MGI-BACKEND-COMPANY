from django.contrib import admin
from django.utils.html import format_html
from .models import TradeReasons

@admin.register(TradeReasons)
class TradeReasonsAdmin(admin.ModelAdmin):
    list_display = (
        'user', 
        'traders_idea_name',
        'currency_pair', 
        'trade_signal', 
        'is_active', 
        'created_at', 
        'idea_candle_image', 
        'idea_candle_two_image', 
        'youtube_candle_image', 
        'volumetic_rejection_candle_image', 
        'fibonnaci_candle_image', 
        'ICT_killzone_candle_image', 
        'ichimoku_candle_image', 
        'ema_cross_alert_candle_image', 
        'ICT_institutional_order_candle_image', 
        'daily_high_low_candle_image', 
        'all_indicators_candle_image', 
        'blog_trade_post_candle_image', 
        'blog_mt5_post_candle_image', 
        'stoploss_candle_image'
    )
    
    list_filter = ('traders_idea_name', 'trade_signal', 'is_active', 'created_at')
    search_fields = ('user__username', 'currency_pair')
    readonly_fields = ('created_at',)
    
    fieldsets = (
        (None, {
            'fields': ('user', 'traders_idea_name', 'currency_pair', 'trade_signal', 'is_active', 'created_at')
        }),
        ('Custom Candles', {
            'fields': (
                'idea_candle',
                'idea_candle_two',
                'youtube_candle',
                'volumetic_rejection_candle',
                'fibonnaci_candle',
                'ICT_killzone_candle',
                'ichimoku_candle',
                'ema_cross_alert_candle',
                'ICT_institutional_order_candle',
                'daily_high_low_candle',
                'all_indicators_candle',
                'blog_trade_post_candle',
                'blog_mt5_post_candle',
                'stoploss_candle',
            ),
        }),
    )

    def image_thumbnail(self, obj, field_name):
        field = getattr(obj, field_name)
        if field:
            return format_html('<img src="{}" width="50" height="50" />', field.url)
        return None

    def idea_candle_image(self, obj): return self.image_thumbnail(obj, 'idea_candle')
    def idea_candle_two_image(self, obj): return self.image_thumbnail(obj, 'idea_candle_two')
    def youtube_candle_image(self, obj): return self.image_thumbnail(obj, 'youtube_candle')
    def volumetic_rejection_candle_image(self, obj): return self.image_thumbnail(obj, 'volumetic_rejection_candle')
    def fibonnaci_candle_image(self, obj): return self.image_thumbnail(obj, 'fibonnaci_candle')
    def ICT_killzone_candle_image(self, obj): return self.image_thumbnail(obj, 'ICT_killzone_candle')
    def ichimoku_candle_image(self, obj): return self.image_thumbnail(obj, 'ichimoku_candle')
    def ema_cross_alert_candle_image(self, obj): return self.image_thumbnail(obj, 'ema_cross_alert_candle')
    def ICT_institutional_order_candle_image(self, obj): return self.image_thumbnail(obj, 'ICT_institutional_order_candle')
    def daily_high_low_candle_image(self, obj): return self.image_thumbnail(obj, 'daily_high_low_candle')
    def all_indicators_candle_image(self, obj): return self.image_thumbnail(obj, 'all_indicators_candle')
    def blog_trade_post_candle_image(self, obj): return self.image_thumbnail(obj, 'blog_trade_post_candle')
    def blog_mt5_post_candle_image(self, obj): return self.image_thumbnail(obj, 'blog_mt5_post_candle')
    def stoploss_candle_image(self, obj): return self.image_thumbnail(obj, 'stoploss_candle')
    
    idea_candle_image.short_description = 'Idea Candle'
    idea_candle_two_image.short_description = 'Idea Candle Two'
    youtube_candle_image.short_description = 'Youtube Candle'
    volumetic_rejection_candle_image.short_description = 'Volumetic Rejection Candle'
    fibonnaci_candle_image.short_description = 'Fibonacci Candle'
    ICT_killzone_candle_image.short_description = 'ICT Killzone Candle'
    ichimoku_candle_image.short_description = 'Ichimoku Candle'
    ema_cross_alert_candle_image.short_description = 'EMA Cross Alert Candle'
    ICT_institutional_order_candle_image.short_description = 'ICT Institutional Order Candle'
    daily_high_low_candle_image.short_description = 'Daily High Low Candle'
    all_indicators_candle_image.short_description = 'All Indicators Candle'
    blog_trade_post_candle_image.short_description = 'Blog Trade Post Candle'
    blog_mt5_post_candle_image.short_description = 'Blog MT5 Post Candle'
    stoploss_candle_image.short_description = 'Stoploss Candle'
