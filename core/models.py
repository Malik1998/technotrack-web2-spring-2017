from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class DateOfCreation(models.Model):
    dateOfCreation = models.DateField()

    class Meta:
        abstract = True


class DateOfEditing(models.Model):
    dateOfEditing = models.DateField()

    class Meta:
        abstract = True


class Authored(models.Model):
    user = models.ForeignKey(User)

    class Meta:
        abstract = True
