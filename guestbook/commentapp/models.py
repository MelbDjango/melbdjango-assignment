from django.db import models

# Create your models here.
class GuestPost(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(blank=True)
    show = models.BooleanField(default=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    comment = models.TextField()

    def __str__(self):
        return '{} [{}] - {} {}'.format(self.name, self.email, self.pub_date, self.comment)

    def is_visible(self):
        return self.show
