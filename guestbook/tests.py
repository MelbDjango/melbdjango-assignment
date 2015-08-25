from django.test import TestCase

# Create your tests here.


class GuestbookViewTestCase(TestCase):
    fixtures = ['guestbook_views_testdata.json']

    def test_redirect(self):
        """
        Check that our root redirect works
        """
        response = self.client.get('/')
        self.assertRedirects(response, '/guestbook/', target_status_code=200)

    def test_guestbook_index(self):
        """
        Check the guestbook list:
            - guest_comments is in our context and contains only ßnon-hidden comments
            - check a couple of non-hidswn entries to ensure the data is there
        """
        response = self.client.get('/guestbook/')
        self.assertTrue(response.status_code, 200)
        self.assertTrue('guest_comments' in response.context)
        guest_comments = response.context['guest_comments']
        self.assertEqual(set([comment.pk for comment in guest_comments]), {1, 2, 4})
        for comment in guest_comments:
            if comment.pk == 1:
                self.assertEqual(comment.name, "Joe Bloggs")
                self.assertEqual(comment.email, "joe@bloggs.net")
                self.assertFalse(comment.comment)
            if comment.pk == 4:
                self.assertEqual(comment.name, "John Doe")
                self.assertEqual(comment.email, "john@doe.net")
                self.assertTrue(comment.comment)

    def test_404(self):
        """
        Make sure we get a 404 from a non-valid url
        This also ensures that we have a working production setup
        """
        response = self.client.get('/this-does-not-exist/')
        self.assertTrue(response.status_code, 404)
