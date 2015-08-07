from django.db import models

class Comment(models.Model):
    name = models.CharField(max_length=255)
    email_address = models.EmailField(max_length=254, blank=True, help_text="optional")
    comment = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    hide = models.BooleanField(default=False)

    def __str__(self):
        email_str = " ({})".format(self.email_address) if self.email_address else ""
        return "<Comment: {}{} created {}>".format(self.name, email_str, self.created)

class SpamString(models.Model):
    s = models.CharField(max_length=255, verbose_name="Spam substring")

    def __str__(self):
        return "<SpamString: {}>".format((self.s))
