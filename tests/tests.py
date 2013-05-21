# -*- coding: utf8 -*-
from random import randint
from django.conf import settings
from django.test.utils import override_settings
from django.utils import unittest
from memento.helpers import Logger
from memento.models import LogEntry, Event


class TestLoginCodes(unittest.TestCase):
    def setUp(self):
        self.obj = object()

    def test_log_simple_message(self):

        message = "this is a simple message"
        Logger.log(message)

        self.assertEqual(len(Event.objects.all()), 1)
        self.assertEqual(len(LogEntry.objects.all()), 1)

    def test_log_object_message(self):
        message = "this is random test message %s" % randint(0, 100)
        Logger.log(message, self.obj)
        self.assertEqual(LogEntry.objects.all()[0].message, message)

    def test_get_log_object_message(self):
        message = "this is random test message %s" % randint(0, 100)
        Logger.log(message, self.obj)
        self.assertEqual(Logger.get_log(self.obj)[0].message, message)

    def tearDown(self):
        LogEntry.objects.all().delete()
        Event.objects.all().delete()