# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Messages(models.Model):
    MsgId = models.AutoField(primary_key=True)
    Unixtime = models.IntegerField()
    Username = models.CharField(max_length=20)
    MessagesString = models.CharField(max_length=100)
