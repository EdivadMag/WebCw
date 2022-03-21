from django.conf import settings
from django.db import models
from django.utils import timezone


class Module(models.Model):
    code = models.CharField(max_length=3, default='000', unique=True)
    name = models.CharField(max_length=30)
    year = models.IntegerField(default=2022)

    def __str__(self):
        return f"Module(code={self.code}, name={self.name})"
