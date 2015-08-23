from django.test import TestCase
from datetime import timedelta

from .models import GuestPost


class TestViews(TestCase):

    name = 'Guest Name'
    comment = 'This is awesome!'
    valid_email = 'guest@geocities.com'
    invalid_email = 'ggg..$%$#sdlfkj%%'

    def test_createWithoutEmail(self):
        data = {
            'name': self.name,
            'comment': self.comment
        }
        response = self.client.post('/', data, follow=True)
        self.assertRedirects(response, '/thankyou/', 302, 200)
        response = self.client.get('/')
        self.assertContains(response, data['name'])
        self.assertContains(response, data['comment'])
        self.assertContains(response, "published Just now")

    def test_createWithValidEmail(self):
        data = {
            'name': self.name,
            'email': self.valid_email,
            'comment': self.comment
        }
        response = self.client.post('/', data, follow=True)
        self.assertRedirects(response, '/thankyou/', 302, 200)
        response = self.client.get('/')
        self.assertContains(response, data['name'])
        self.assertContains(response, data['comment'])
        self.assertContains(response, "published Just now")

    def test_createWithInvalidEmail(self):
        data = {
            'name': self.name,
            'email': self.invalid_email,
            'comment': self.comment
        }
        response = self.client.post('/', data, follow=True)
        self.assertContains(response, "Enter a valid email address.")

    def test_postCreatedWithDate(self):
        data = {
            'name': self.name,
            'email': self.valid_email,
            'comment': self.comment
        }
        response = self.client.post('/', data, follow=True)
        self.assertRedirects(response, '/thankyou/', 302, 200)
        recent_post = GuestPost.objects.get(pk=1)
        self.assertTrue(recent_post.pub_date is not None)

    def test_postCreatedFiveDaysAgo(self):
        data = {
            'name': self.name,
            'email': self.valid_email,
            'comment': self.comment
        }
        response = self.client.post('/', data, follow=True)
        self.assertRedirects(response, '/thankyou/', 302, 200)
        response = self.client.get('/')
        self.assertContains(response, 'published Just now')
        recent_post = GuestPost.objects.get(pk=1)
        five_days = timedelta(days=5)
        recent_post.pub_date = recent_post.pub_date - five_days
        recent_post.save()
        response = self.client.get('/')
        self.assertContains(response, 'published 5 days ago')

    def test_postCounterDisplay(self):
        for i in range(5):
            GuestPost.objects.create(name='guest{}'.format(i), comment='{}'.format(i))
        response = self.client.get('/')
        self.assertContains(response, "5 guests posted on MelbDjango")

    def test_postNowYouSeeItNowYouDont(self):
        GuestPost.objects.create(name=self.name, comment=self.comment)
        response = self.client.get('/')
        self.assertContains(response, self.name)
        self.assertContains(response, self.comment)
        recent_post = GuestPost.objects.get(pk=1)
        recent_post.show = False
        recent_post.save()
        response = self.client.get('/')
        self.assertNotContains(response, self.name)
        self.assertNotContains(response, self.comment)

    def test_postSpammyContent(self):
        self.comment = "hi Melbdjango i promise you, with this program weight loss is 100% guaranteed."
        data = {
            'name': self.name,
            'comment': self.comment
        }
        response = self.client.post('/', data, follow=True)
        self.assertContains(response, "Your post smells spammy.")
