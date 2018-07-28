# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import  UserInfo, Profile, Notification

admin.site.register(UserInfo)
admin.site.register(Profile)
admin.site.register(Notification)



# Register your models here.
