from django.utils import timezone

from django.db import models


#display optional on email field including back-end
EMAIL_OPTIONAL = ('*optional')

#hide and show record entries at front-end for the form field display
BOOL_CHOICES = ((True, 'Show'), (False, 'Hide'))


class Record(models.Model):
    class Meta:
        verbose_name_plural = 'records'
    
    first_name =models.CharField(blank=False, max_length=40, verbose_name ='First Name') 
    last_name = models.CharField(blank=False, max_length=40, verbose_name='Last Name')
    comment = models.CharField(blank=False, max_length=400)
    email_address = models.EmailField(blank=True, max_length=40, help_text=EMAIL_OPTIONAL)
    entry_date = models.DateTimeField(default=timezone.now) 
    display = models.BooleanField(default=True, choices=BOOL_CHOICES)
   
    def __str__(self):
        return '<{}> {}'.format(self.first_name, self.last_name, self.comment, self.email_address, self.entry_date, self.display)
