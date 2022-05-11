from django.contrib import admin

from .models import Note


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'public', 'update_ad', 'id')

    fields = (('title', 'public'), 'message', 'create_at', 'update_ad')

    readonly_fields = ('create_at', 'update_ad')

    search_fields = ['title']

    list_filter = ('public', "message")
