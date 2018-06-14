import datetime

from django.db import models
from django.utils import timezone

class homemenu(models.Model):
    class Meta:
        verbose_name = 'Menu Option'
        verbose_name_plural = 'Menu Options'
    menu_text = models.CharField('Menu Option', max_length=200)
    def __str__(self):
        return self.menu_text