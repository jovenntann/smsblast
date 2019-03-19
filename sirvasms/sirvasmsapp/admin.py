# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from sirvasmsapp.models import Received
from sirvasmsapp.models import DateRange
from sirvasmsapp.models import Rate
from sirvasmsapp.models import Queue, QueueBlast
from sirvasmsapp.models import Contact
from sirvasmsapp.models import Goip
from sirvasmsapp.models import Prov
from sirvasmsapp.models import Prefix

admin.site.register(Received)
admin.site.register(DateRange)
admin.site.register(Rate)
admin.site.register(Queue)
admin.site.register(QueueBlast)
admin.site.register(Contact)
admin.site.register(Goip)
admin.site.register(Prov)
admin.site.register(Prefix)