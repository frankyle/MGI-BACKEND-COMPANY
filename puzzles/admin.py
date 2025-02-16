from django.contrib import admin
from django.utils.html import format_html
from .models import Puzzle

@admin.register(Puzzle)
class PuzzleAdmin(admin.ModelAdmin):
    # Display these fields in the list view
    list_display = (
        'name', 
        'description', 
        'price', 
        'stock', 
        'sold', 
        'remaining_stock', 
        'pieces', 
        'age_group', 
        'rating', 
        'user', 
        'puzzle_image_thumbnail'
    )
    
    # Filters to narrow down records
    list_filter = ('age_group', 'rating', 'user')
    
    # Search by name or description
    search_fields = ('name', 'description', 'user__username')
    
    # Field organization in the form view
    fieldsets = (
        (None, {
            'fields': (
                'name', 
                'description', 
                'price', 
                'stock', 
                'sold', 
                'pieces', 
                'age_group', 
                'rating', 
                'user', 
                'image'
            )
        }),
    )
    
    # Read-only fields
    readonly_fields = ('remaining_stock', 'puzzle_image_thumbnail')
    
    # Custom thumbnail display for the image field
    def puzzle_image_thumbnail(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
        return "No Image"
    puzzle_image_thumbnail.short_description = "Puzzle Image Thumbnail"

    # Ordering puzzles by rating (highest first)
    ordering = ('-rating',)
