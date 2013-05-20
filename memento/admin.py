# -*- coding: utf8 -*-
from django.contrib import admin
from memento.models import LogEntry, Event


class EventInline(admin.TabularInline):
    model = Event
    readonly_fields = ('timestamp',)


class LogEntryAdmin(admin.ModelAdmin):
    list_display = ('message', 'severity', 'last_timestamp')
    readonly_fields = ('message', 'severity', 'last_timestamp')
    fields = ('message', 'severity', 'last_timestamp')

    def has_add_permission(self, request):
        return False

admin.site.register(LogEntry, LogEntryAdmin)