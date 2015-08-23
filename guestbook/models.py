from time import strftime, localtime
from django.db import models

# Create your models here.


class GuestComment(models.Model):
    """
    Guestbook comment

    Comments are shown by default.
    Hidden status may also be set by the spam or profanity checks.
    """
    email = models.EmailField(default=None)
    name = models.CharField(max_length=60)
    entrydate = models.DateTimeField(auto_now=True, db_index=True)
    hidden = models.BooleanField(default=False)
    comment = models.TextField(blank=True)

    def __str__(self):
        return "%s%s <%s> %s %.25s" % \
               ('[hidden] ' if self.hidden else '',
                self.entrydate.strftime("%Y-%m-%d %H:%M"),
                self.email, self.name,
                self.comment.replace("\n", " "))
