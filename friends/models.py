from __future__ import unicode_literals

from django.db import models


# Create your models here.
from core.models import User


class Friends(models.Model):
    firstFriend = models.ForeignKey(User, related_name='firstFriend')
    secondFriend = models.ForeignKey(User, related_name='secondFriend')
