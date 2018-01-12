from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from rest_framework import serializers
from datetime import datetime

# /////////////////////////////////////////////////
# Option menu's
# /////////////////////////////////////////////////

class Action(models.Model):
    action_id = models.AutoField(primary_key=True)
    action = models.CharField(max_length=255, null=True)
    date_upload = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return '{}'.format(self.action)

    class Meta:
        db_table = 'action'


class RawCapture(models.Model):
    cap_id = models.AutoField(primary_key=True)
    action = models.ForeignKey(Action,
                            related_name='action_name',
                            on_delete=models.CASCADE,
                            null=True, blank=True)
    RawCapture = models.CharField(max_length=255, null=True)

    def Action(self):
        return '{}'.format(self.action.action)

    def __str__(self):
        return '{} - {}'.format(self.action, self.Raw)

    class Meta:
        db_table = 'capture_raw'