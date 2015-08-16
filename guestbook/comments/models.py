from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.utils import timezone

# Create your models here.

class Comment(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=1024)
    created_at = models.DateTimeField(default=timezone.now)
    is_public = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return '<{}> {}'.format(self.author, self.title)

    def get_absolute_url(self):
        return reverse('comments_detail', kwargs={'pk': self.pk})


class Message(models.Model):
    text = models.CharField(max_length=200)
    user = models.ForeignKey(User)
    comment = models.ForeignKey('Comment')

    def __str__(self):
        return '<{}> {}'.format(self.user, self.text)
        
