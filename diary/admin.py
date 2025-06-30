from django.contrib import admin

from .models import Entry, Tag


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'mood', 'owner')
    list_display_links = ('id', 'title')
    ordering = [
        '-created_at',
    ]
    list_per_page = 10


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'owner')
    list_display_links = ('id', 'name')
