from django.contrib import admin
from django.utils.html import format_html
from .models import RiskTrade

@admin.register(RiskTrade)
class RiskTradeAdmin(admin.ModelAdmin):
    def mt5_chart_preview(self, obj):
        """Display a preview of the MT5 chart image."""
        if obj.mt5_chart:
            return format_html('<img src="{}" width="100" height="100" style="object-fit: cover; border-radius: 5px;" />', obj.mt5_chart.url)
        return "No Image"

    def tradeview_chart_preview(self, obj):
        """Display a preview of the TradeView chart image."""
        if obj.tradeview_chart:
            return format_html('<img src="{}" width="100" height="100" style="object-fit: cover; border-radius: 5px;" />', obj.tradeview_chart.url)
        return "No Image"

    def mt5_positions_preview(self, obj):
        """Display a preview of the MT5 Positions image."""
        if obj.mt5_positions:
            return format_html('<img src="{}" width="100" height="100" style="object-fit: cover; border-radius: 5px;" />', obj.mt5_positions.url)
        return "No Image"

    mt5_chart_preview.short_description = "MT5 Chart"
    tradeview_chart_preview.short_description = "TradeView Chart"
    mt5_positions_preview.short_description = "MT5 Positions"

    list_display = ('currency_pair', 'user', 'risk_pips', 'risk_dollars', 'risk_tsh', 
                    'gain_pips', 'gain_dollars', 'gain_tsh', 'date', 'day_name', 
                    'created_at', 'updated_at', 'mt5_chart_preview', 'tradeview_chart_preview', 'mt5_positions_preview')
    
    list_filter = ('currency_pair', 'user', 'created_at', 'date', 'day_name')
    search_fields = ('currency_pair', 'user__username', 'date', 'day_name')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at', 'mt5_chart_preview', 
                       'tradeview_chart_preview', 'mt5_positions_preview', 'date', 'day_name')

    fieldsets = (
        ('Trade Details', {
            'fields': ('currency_pair', 'risk_pips', 'risk_dollars', 'risk_tsh', 
                       'gain_pips', 'gain_dollars', 'gain_tsh', 'date', 'day_name')
        }),
        ('Charts & Images', {
            'fields': ('mt5_chart', 'mt5_chart_preview', 
                       'tradeview_chart', 'tradeview_chart_preview', 
                       'mt5_positions', 'mt5_positions_preview')
        }),
        ('User & Timestamps', {
            'fields': ('user', 'created_at', 'updated_at')
        }),
    )

    def get_readonly_fields(self, request, obj=None):
        """Ensure image previews and date-related fields remain read-only when editing."""
        readonly_fields = super().get_readonly_fields(request, obj)
        if obj:  # Editing an existing object
            return readonly_fields + ('mt5_chart_preview', 'tradeview_chart_preview', 'mt5_positions_preview', 'date', 'day_name')
        return readonly_fields
