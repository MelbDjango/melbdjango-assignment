from django.db import models
from django.utils import timezone


# Create your models here.
class Record(models.Model):
    class Meta:
        verbose_name_plural = 'records'

    EMAIL_FORMAT = ('you@example.com')

    name = models.CharField(max_length=200, default='Your awesome name') 
    comment = models.CharField(max_length =2000)
    email_address = models.EmailField(helptext=EMAIL_FORMAT)
    entry_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '<{}> {}'.format(self.name, self.comment, self.email_address, self.entry_date)