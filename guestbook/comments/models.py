from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.utils import timezone
from math import trunc

# Create your models here.

def calc_long_ago(created_at):
    delta = timezone.now() - created_at
    print(created_at, timezone.now(), delta.seconds)
    if delta.days > 15:
        return "a while ago"
    else:
        if delta.days > 1:
            t = trunc(delta.days)
            return "{:d} day{} ago".format(t, "" if t > 1 else "s")
        else:
            if delta.seconds > 3600:
                t = trunc(delta.seconds/60/60)
                return "{:d} hours ago".format(t, "" if t > 1 else "s")

            elif delta.seconds > 300:
                t = trunc(delta.seconds/60)
                return "{:d} minute{} ago".format(t, "" if t > 1 else "s")
            else:
                return "just now"

class Comment(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=1024)
    created_at = models.DateTimeField(default=timezone.now)
    is_public = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    def long_ago(self):
        return calc_long_ago(self.created_at)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return '<{}> {}'.format(self.author, self.title)

    def get_absolute_url(self):
        return reverse('comments_detail', kwargs={'pk': self.pk})


class Message(models.Model):
    text = models.CharField(max_length=200)
    user = models.ForeignKey(User)
    comment = models.ForeignKey('Comment')
    created_at = models.DateTimeField(default=timezone.now)
    is_public = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_spam = models.BooleanField(default=False)

    def long_ago(self):
        return calc_long_ago(self.created_at)


    def __str__(self):
        return '<{}> {}'.format(self.user, self.text)
