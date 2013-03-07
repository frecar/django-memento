from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.db import models


class LogEntry(models.Model):
    message = models.TextField()
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')


    @property
    def count(self):
        return self.events.objects.all().count()


class Events(models.Model):
    entry = models.ForeignKey(LogEntry, related_name='events')
    timestamp = models.DateTimeField()

    class Meta:
        ordering = ( 'entry', '-timestamp')