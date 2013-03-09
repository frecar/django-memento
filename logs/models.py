# -*- coding: utf8 -*-
from django.conf import settings
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.db import models

from logs import choices


class LogEntry(models.Model):
    message = models.TextField()
    content_type = models.ForeignKey(ContentType, related_name='log_entries')
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')
    severity = models.IntegerField(choices=getattr(settings, 'LOGS_SEVERITY_CHOICES', choices.SEVERITIES))
    last_timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-last_timestamp',)

    @property
    def count(self):
        return self.events.objects.all().count()

    def add_event(self):
        Event.objects.create(entry=self)


class Event(models.Model):
    entry = models.ForeignKey(LogEntry, related_name='events', editable=False)
    timestamp = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        ordering = ( 'entry', '-timestamp')