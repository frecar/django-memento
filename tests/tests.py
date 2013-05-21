# -*- coding: utf8 -*-
from random import randint
from django.utils import unittest
from memento.helpers import Logger
from memento.models import LogEntry, Event
from models import Message


class TestLoginCodes(unittest.TestCase):
    def setUp(self):
        self.obj = Message()
        self.obj.save()

    def test_log_simple_message(self):

        message = "this is a simple message"
        Logger.log(message)

        self.assertEqual(len(Event.objects.all()), 1)
        self.assertEqual(len(LogEntry.objects.all()), 1)

    def test_log_simple_message_multiple_times(self):

        message = "this is a simple message"
        Logger.log(message)
        Logger.log(message)
        Logger.log(message)

        self.assertEqual(len(Event.objects.all()), 1)
        self.assertEqual(len(LogEntry.objects.all()), 3)

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