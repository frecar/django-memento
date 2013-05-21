# -*- coding: utf8 -*-
from django.utils.translation import ugettext_lazy as _
from memento.helpers import Logger

SEVERITIES = (
    (1, _('Very low')),
    (2, _('Low')),
    (3, _('Medium')),
    (4, _('High')),
    (5, _('Very High')),
)

Logger.get_log

