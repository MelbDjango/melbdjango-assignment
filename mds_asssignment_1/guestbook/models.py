from django.db import models
import datetime

class Entry(models.Model):
    fname = models.CharField(max_length=50, verbose_name='First Name')
    lname = models.CharField(max_length=50, verbose_name='Last Name')
    email = models.CharField(max_length=100)
    comment = models.CharField(max_length=500)
    date = models.DateTimeField()
    visible = models.BooleanField(default=True)

    def __str__(self):
        return self.comment

    def age(self):
        # Returns a string with how old the entry is
        td = datetime.datetime.now(datetime.timezone.utc) - self.date
        s = td.total_seconds()
        hours, remainder = divmod(s, 3600)
        minutes, seconds = divmod(remainder, 60)
        return '{} hours, {} minutes, {} seconds ago.'.format(*map(int, (hours, minutes, seconds)))
