#!/usr/bin/env python

import os
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    args = ''
    help = 'Creates superuser'

    def handle(self, *args, **options):
        """
        Creates superuser if environment variables are set
        """
        User = get_user_model()

        username = os.environ.get('ADMIN_USERNAME')
        password = os.environ.get('ADMIN_PASSWORD')

        if username and password:
          if User.objects.count() == 0:
              admin = User.objects.create(username=username)
              admin.set_password(password)
              admin.is_superuser = True
              admin.is_staff = True
              admin.save()


