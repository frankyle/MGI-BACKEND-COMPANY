from django.contrib import admin
from django.utils.html import format_html
from .models import Toy

@admin.register(Toy)
class ToyAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = (
        'name',
        'description',
        'price',
        'stock',
        'sold',
        'remaining_stock',
        'pieces',
        'category',
        'age_group',
        'rating',
        'user',
        'toy_image_thumbnail'
    )
    
    # Filters for easy navigation
    list_filter = ('category', 'age_group', 'rating', 'user')
    
    # Enable search by name and user
    search_fields = ('name', 'description', 'user__username')
    
    # Organize fields into sections
    fieldsets = (
        (None, {
            'fields': (
                'name',
                'description',
                'price',
                'stock',
                'sold',
                'pieces',
                'category',
                'age_group',
                'rating',
                'user',
                'image'
            )
        }),
    )
    
    # Read-only fields
    readonly_fields = ('remaining_stock', 'toy_image_thumbnail')
    
    # Custom thumbnail display for the toy image
    def toy_image_thumbnail(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
        return "No Image"
    toy_image_thumbnail.short_description = "Toy Image Thumbnail"

    # Default ordering by rating in descending order
    ordering = ('-rating',)
