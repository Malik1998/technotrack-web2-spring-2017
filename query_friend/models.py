from __future__ import unicode_literals

from django.db import models

# Create your models here.
from core.models import User


class QueryFriend(models.Model):
    requester = models.ForeignKey(User, related_name='requester')
    responser = models.ForeignKey(User, related_name='responser')
    signed = models.BooleanField()