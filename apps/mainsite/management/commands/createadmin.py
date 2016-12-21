#!/usr/bin/env python

import os
from django.contrib.auth.models import User

username = os.environ.get('ADMIN_USERNAME')
password = os.environ.get('ADMIN_PASSWORD')

if username and password:
  if User.objects.count() == 0:
      admin = User.objects.create(username=username)
      admin.set_password(password)
      admin.is_superuser = True
      admin.is_staff = True
      admin.save()
