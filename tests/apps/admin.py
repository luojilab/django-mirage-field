from django.contrib import admin
from django.contrib.admin.models import LogEntry
from .models import TestModel


@admin.register(LogEntry)
class DjangoLogAdmin(admin.ModelAdmin):
    list_display = ['id', 'content_type', 'user',
                    'object_repr', 'change_message', 'action_time']
    search_fields = ['user_id']


@admin.register(TestModel)
class DjangoLogAdmin(admin.ModelAdmin):
    list_display = ['id', 'char', 'text', 'textraw', 'integer', 'email']
    search_fields = ['id', 'char', 'text', 'textraw', 'integer', 'email']
