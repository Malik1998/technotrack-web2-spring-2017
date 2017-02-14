from __future__ import unicode_literals

from django.db import models

# Create your models here.
from core.models import DateOfCreation, DateOfEditing, User


class Like(DateOfCreation, DateOfEditing):
    user = models.ForeignKey(User)
