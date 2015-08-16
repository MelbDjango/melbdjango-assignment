from django.db import models
from django.utils import timezone


STATUS_CHOICES = (
	('h', 'Hidden'),
	('p', 'Published'),
	)

class Post(models.Model):
	name = models.CharField(max_length=150)
	text = models.TextField()
	email = models.EmailField(max_length=254, blank=True, null=True)
	time = models.DateTimeField(default=timezone.now)
	status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='p')	


	def __str__(self):
		#I just copied this format from the timetracker example, not sure if it is required...
		return '{} {}'.format(self.name, self.text)


# Create your models here.
