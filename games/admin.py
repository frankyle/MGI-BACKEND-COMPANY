from django.contrib import admin
from django.utils.html import format_html
from .models import Game

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = (
        'name',
        'category',
        'price',
        'stock',
        'sold',
        'remaining_stock',
        'rating',
        'user',
        'created_at',
        'updated_at',
        'game_image_thumbnail',
    )

    # Filters for easy navigation
    list_filter = ('category', 'rating', 'user', 'created_at')

    # Enable search by game name and user
    search_fields = ('name', 'description', 'user__username')

    # Organize fields into sections
    fieldsets = (
        (None, {
            'fields': ('name', 'description', 'price', 'category', 'image')
        }),
        ('Stock Information', {
            'fields': ('stock', 'sold', 'remaining_stock')
        }),
        ('Additional Information', {
            'fields': ('rating', 'user', 'created_at', 'updated_at')
        }),
    )

    # Read-only fields
    readonly_fields = ('remaining_stock', 'created_at', 'updated_at', 'game_image_thumbnail')

    # Custom thumbnail display for the game image
    def game_image_thumbnail(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
        return "No Image"
    game_image_thumbnail.short_description = "Game Image"

    # Default ordering
    ordering = ('-created_at',)
