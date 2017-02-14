from __future__ import unicode_literals

from django.db import models


# Create your models here.
from core.models import User


class Chat(models.Model):
    user = models.ForeignKey(User)
    chatId = models.IntegerField()
    #
    # class Meta:
    #     model = ListOfUsersInChat


class ListOfUsersInChat(models.Model):
    user = models.ForeignKey(User)
    chatId = models.ForeignKey(Chat)