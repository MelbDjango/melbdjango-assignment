import datetime as dt
import random import randint
from django.template.defaultfilters import slugify
from factory import DjangoModelFactory, lazy_attribute

class UserFactory(DjangoModelFactory):
    class Meta:
        model = 'auth.User'
        django_get_or_create = ('username',)

        username = 'John'
        email = lazy_attribute(lambda o: o.username + "@example.com")

        @lazy_attribute
        def date_joined(self):
            return dt.datetime.now() - dt.timedelta(days=randint(5, 50))
        last_login = lazy_attribute(lambda o: o.date_joined + dt.timedelta(days=4))
