from __future__ import unicode_literals

from django.db import models

# Create your models here.
from chat.models import Chat
from core.models import User


class Message(models.Model):
    user = models.ForeignKey(User)
    text = models.TextField()
    chatId = models.ForeignKey(Chat)
