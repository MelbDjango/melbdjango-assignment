from django.db import models

class Entry(models.Model):
    fname = models.CharField(max_length=50, verbose_name='First Name')
    lname = models.CharField(max_length=50, verbose_name='Last Name')
    email = models.CharField(max_length=100)
    comment = models.CharField(max_length=500)
    date = models.DateTimeField()
    visible = models.BooleanField(default=True)

    def __str__(self):
        return self.comment
