# -*- coding: utf8 -*-
from django.contrib.contenttypes.models import ContentType

from memento.models import LogEntry


class Logger(object):

    @staticmethod
    def log(self, message, obj=None, severity=None):
        """
        Create LogEntry for object with message and severity

        message: a string
        object: can be a model
        severity is a number from 1-5

        1: Very low
        2: Low
        3: Medium
        4: High
        5: Very High


        :type message str
        :type obj object
        :type severity int
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

    @staticmethod
    def get_log(self, obj, severity=None):
        """
        :type obj object
        :type severity int
        """
        return LogEntry.objects.filter(
            content_type=ContentType.objects.get_for_model(obj),
            object_id=obj.id,
            severity=severity
        )