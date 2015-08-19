from django.test import TestCase, Client
from django.utils import timezone
from django.core.urlresolvers import reverse

from .forms import is_spam
from .views import get_valid_posts
from .models import Post


class FormTests(TestCase):
    def test_is_spam(self):
        """
        Ensure the is_spam function returns True for common forms of spam.
        """
        text = 'lose weight'
        self.assertTrue(is_spam(text))
        text = '100% free'
        self.assertTrue(is_spam(text))
        text = 'dear friend'
        self.assertTrue(is_spam(text))
        text = 'hello'
        self.assertFalse(is_spam(text))


class ViewTests(TestCase):
    def create_post(self, name, text, email, hidden_at):
        """
        Helper method to create a post.
        """
        post = Post()
        post.name = name
        post.text = text
        post.email = email
        post.hidden_at = hidden_at
        post.save()
        return post

    def test_get_valid_posts(self):
        """
        Create 2 posts, one valid one invalid. Check that only the valid one
        is in the valid posts list.
        """
        post = self.create_post('Karl',
                                'Hello',
                                'karl@example.com',
                                None)
        self.create_post('Karl',
                         'Hello',
                         'karl@example.com',
                         timezone.now())
        post_list = get_valid_posts()
        self.assertEqual(len(post_list), 1)
        self.assertEqual(post_list[0].pk, post.pk)

    def test_list_no_posts(self):
        """
        Test that the guestbook view shows "No posts." when there aren't
        any posts.
        """
        client = Client()
        url = reverse('guestbook:post-create-list')
        response = client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No posts.')

    def test_list_5_posts(self):
        """
        Test that the guestbook view shows the correct number of posts.
        """
        for i in range(5):
            self.create_post('yo',
                             'yea boy',
                             'hello@example.com',
                             None)
        client = Client()
        url = reverse('guestbook:post-create-list')
        response = client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['posts']), 5)
