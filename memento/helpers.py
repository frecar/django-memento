# -*- coding: utf8 -*-
from django.contrib.contenttypes.models import ContentType

from memento.models import LogEntry


class Logger(object):

    def log(self, message, obj=None, severity=None):
        if not obj is None:
            entry = LogEntry.objects.get_or_create(
                message=message,
                content_type=ContentType.objects.get_for_model(obj),
                object_id=obj.id,
                severity=severity
            )
        else:
            entry = LogEntry.objects.get_or_create(
                message=message,
                severity=severity
            )

        entry.add_event()