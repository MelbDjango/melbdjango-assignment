from django.db import models
from django.utils import timezone


STATUS_CHOICES = (
	('h', 'Hidden'),
	('p', 'Published'),
	)

class Post(models.Model):
	name = models.CharField(max_length=150)
	text = models.TextField()
	email = models.EmailField(max_length=254)
	time = models.DateTimeField(default=timezone.now)
	status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='p')
	

	def make_post(self):
		self.save()


	def count_post(self):
		pass

	def __str__(self):
		return '{} {}'.format(self.name, self.text)


# Create your models here.
