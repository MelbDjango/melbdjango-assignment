import datetime as dt
import random import randint
from django.template.defaultfilters import slugify
from factory import DjangoModelFactory, SubFactory, FuzzyText, fuzzy, lazy_attribute

from register.factories import UserFactory

from .models import Comment, Message

class CommentFactory(DjangoModelFactory):

    author = SubFactory(UserFactory)

    @lazy_attribute
    def created_at(self):
        return dt.datetime.now() - dt.timedelta(days=randint(5, 50))

    is_active = True
    is_public = True
    text = FuzzyText(length=200)
    title = FuzzyText(length=20)

    class Meta:
        model = Comment

class MessageFactory(DjangoModelFactory):

    comment = SubFactory(CommentFactory)
    user = SubFactory(UserFactory)
    # TODO make sure message created at is not before Comment created_at
    def created_at(self):
        return dt.datetime.now() - dt.timedelta(days=randint(5, 50))
    is_active = True
    is_public = True
    is_spam = False
    text = FuzzyText(length=20)

    class Meta:
        model = Message
