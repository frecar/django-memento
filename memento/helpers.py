# -*- coding: utf8 -*-
from django.conf import settings
from django.contrib.contenttypes.models import ContentType

from memento.models import LogEntry


class Logger(object):

    def log(self, message, obj=None, severity=getattr(settings, 'MEMENTO_SEVERITY_DEFAULT', 1)):
        """
        Adds a log entry and an event related to that log entry.
        :param message: a string
        :param obj: a model, optional
        :param severity: a integer, optional
        """
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