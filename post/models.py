from __future__ import unicode_literals

from django.db import models

# Create your models here.
from core.models import DateOfCreation, DateOfEditing, Authored


class Post(DateOfCreation, DateOfEditing, Authored):
    title = models.CharField(max_length=255)
    text = models.TextField()
    # pictures videos