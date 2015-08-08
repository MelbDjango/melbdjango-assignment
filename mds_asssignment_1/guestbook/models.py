from django.db import models
from django.utils import timezone

class Entry(models.Model):
    fname = models.CharField(max_length=50, verbose_name='First Name')
    lname = models.CharField(max_length=50, verbose_name='Last Name', blank=True)
    email = models.CharField(max_length=100, blank=True)
    comment = models.CharField(max_length=500)
    date = models.DateTimeField(default=timezone.now)
    visible = models.BooleanField(default=True)

    def __str__(self):
        return self.comment
