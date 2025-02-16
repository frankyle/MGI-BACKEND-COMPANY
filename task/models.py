from django.db import models
from django.conf import settings

class Task(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False, blank=True, null=True)
    image = models.ImageField(upload_to='task_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tasks', null=True, blank=True)
    due_date = models.DateTimeField(null=True, blank=True)
    priority = models.CharField(max_length=10, choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], default='medium', null=True, blank=True)
    notes = models.TextField(blank=True, null=True)
    estimated_time = models.PositiveIntegerField(help_text="Estimated time in minutes", null=True, blank=True)
   
    def __str__(self):
        return self.title
