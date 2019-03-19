# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Default Authentication
from django.contrib.auth.models import User
import datetime

class Received(models.Model):
    date = models.DateTimeField()
    from_number = models.CharField(max_length=80)
    name = models.CharField(max_length=80)
    to_number = models.CharField(max_length=80)
    message = models.CharField(max_length=1000)
    MessageSid = models.CharField(max_length=80)
    status = models.CharField(max_length=80)
    
    def __str__(self):
        return str(self.message)

class Queue(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    dateSent = models.DateTimeField(auto_now_add=True)
    provider = models.CharField(max_length=20)
    name = models.CharField(max_length=80)
    to_number =  models.CharField(max_length=20)
    user = models.CharField(max_length=80)
    message = models.CharField(max_length=1000)
    tag = models.CharField(max_length=80)
    goip = models.CharField(max_length=80)
    flag = models.IntegerField(default=0)

    def __str__(self):
        return str(self.message)

class QueueBlast(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    tag = models.CharField(max_length=80)
    message = models.CharField(max_length=1000)
    status = models.CharField(max_length=80)

    def __str__(self):
        return str(self.tag)
      
class Contact(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=80)
    number = models.CharField(max_length=20)
    group = models.CharField(max_length=80)

    def __str__(self):
        return str(self.group)

class DateRange(models.Model):
    user = models.ForeignKey(User)
    date_from = models.DateField()
    date_to = models.DateField()

    def __str__(self):
        return str(self.user)   
      
class Rate(models.Model):
    code = models.CharField(max_length=10)
    abbreviation = models.CharField(max_length=4)
    country = models.CharField(max_length=50)
    buy = models.DecimalField(max_digits=8, decimal_places=6)
    sell = models.DecimalField(max_digits=8, decimal_places=6)
    route = models.CharField(max_length=20)
    source = models.CharField(max_length=20)
    
    def __str__(self):
        return str(self.country)

# class Provider(models.Model):
#     provider = models.CharField(max_length=80)
#     providerid = models.IntegerField()

#     def __str__(self):
#         return str(self.provider)

class Prefix(models.Model):
    provider = models.CharField(max_length=20)
    prefix = models.CharField(max_length=1000)

    def __str__(self):
        return str(self.provider + " | " + self.prefix)

class Prov(models.Model):
    prov = models.CharField(max_length=30, blank=True, null=True)
    inter = models.CharField(max_length=10, blank=True, null=True)
    local = models.CharField(max_length=10, blank=True, null=True)
    recharge_ok_r = models.CharField(max_length=64)
    auto_num_ussd = models.CharField(max_length=20)
    num_prefix = models.CharField(max_length=20)
    num_postfix = models.CharField(max_length=20)

    def __str__(self):
        return self.prov

    class Meta:
        managed = False
        db_table = 'prov'


class Goip(models.Model):
    name = models.CharField(unique=True, max_length=64)
    provider = models.IntegerField()
    host = models.CharField(max_length=50)
    port = models.IntegerField()
    password = models.CharField(max_length=64)
    alive = models.IntegerField()
    num = models.CharField(max_length=30)
    signal = models.IntegerField(blank=True, null=True)
    gsm_status = models.CharField(max_length=30)
    voip_status = models.CharField(max_length=30)
    voip_state = models.CharField(max_length=30)
    bal = models.FloatField(blank=True, null=True)
    cellinfo = models.CharField(db_column='CELLINFO', max_length=160)  # Field name made lowercase.
    cgatt = models.CharField(db_column='CGATT', max_length=32)  # Field name made lowercase.
    bcch = models.CharField(db_column='BCCH', max_length=160)  # Field name made lowercase.
    bal_time = models.DateTimeField(blank=True, null=True)
    keepalive_time = models.DateTimeField(blank=True, null=True)
    gsm_login_time = models.DateTimeField(blank=True, null=True)
    gsm_login_time_t = models.IntegerField()
    keepalive_time_t = models.IntegerField()
    remain_time = models.IntegerField()
    imei = models.CharField(max_length=15, blank=True, null=True)
    imsi = models.CharField(max_length=32, blank=True, null=True)
    iccid = models.CharField(max_length=32, blank=True, null=True)
    last_call_record_id = models.IntegerField()
    remain_count = models.IntegerField()
    count_limit = models.IntegerField()
    remain_count_d = models.IntegerField()
    count_limit_d = models.IntegerField()
    group_id = models.IntegerField()
    report_mail = models.CharField(max_length=64)
    fwd_mail_enable = models.IntegerField()
    report_http = models.CharField(max_length=64)
    fwd_http_enable = models.IntegerField()
    carrier = models.CharField(max_length=32)
    auto_num_c = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'goip'
