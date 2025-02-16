from django.contrib import admin
from django.utils.html import format_html
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    def task_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" height="100" style="object-fit: cover; border-radius: 5px;" />', obj.image.url)
        return "No Image"
    task_image.short_description = "Image Preview"

    list_display = ('title', 'user', 'priority', 'due_date', 'completed', 'created_at', 'updated_at', 'task_image')
    list_filter = ('priority',  'completed', 'created_at', 'user')
    search_fields = ('title', 'description', 'user__username')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at', 'task_image')

    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'description', 'image', 'task_image')
        }),
        ('Task Details', {
            'fields': ( 'priority', 'completed', 'due_date', 'estimated_time', 'notes')
        }),
        ('User & Time Tracking', {
            'fields': ('user', 'created_at', 'updated_at')
        }),
    )

    def get_readonly_fields(self, request, obj=None):
        """ Ensure task_image is read-only even when adding a new task """
        readonly_fields = super().get_readonly_fields(request, obj)
        if obj:  # Editing existing object
            return readonly_fields + ('task_image',)
        return readonly_fields

