# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# login user data.
class UserInfo(models.Model):
    uname = models.CharField(max_length=200)
    psw = models.CharField(max_length=200)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.uname

# uploaded data
class Profile(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    share1 = models.CharField(max_length=100)
    share2 = models.CharField(max_length=100)
    picture = models.FileField(upload_to='pictures', blank=True)
    time = models.CharField(max_length=50)

    def __str__(self):
        return self.description

# notification data
class Notification(models.Model):
    doctor = models.CharField(max_length=100)
    nurse = models.CharField(max_length=100)
    reception = models.CharField(max_length=100)