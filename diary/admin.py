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

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def get_queryset(self, request):
        qs = Entry.objects.all()
        qs = qs.select_related("owner")
        return qs


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'owner')
    list_display_links = ('id', 'name')
