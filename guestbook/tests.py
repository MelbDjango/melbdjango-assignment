from django.core.exceptions import ValidationError
from django.test import TestCase

# Create your tests here.
from .forms import GuestbookForm


class GuestbookViewTestCase(TestCase):
    fixtures = ['guestbook_views_testdata.json', 'spamwords_testdata.json']

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
            - check a couple of non-hiden entries to ensure the data is there
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
        self.assertTrue('entries' in response.context)
        self.assertEqual(response.context['entries'], 4)

    def test_404(self):
        """
        Make sure we get a 404 from a non-valid url
        This also ensures that we have a working production setup
        """
        response = self.client.get('/this-does-not-exist/')
        self.assertTrue(response.status_code, 404)

    good = [
        {
            'email': 'test@test.com',
            'name': 'Test User 1',
        },
        {
            'email': 'test2@test.com',
            'name': 'Test User 2',
            'comment': 'Love your site, thanks!',
        },
    ]

    def test_guestbook_entry_good(self):
        """
        First, check a good post via request
        """
        added = 0
        for good in self.good:
            response = self.client.post('/guestbook/', good)
            # ensure we get back a redirect
            self.assertEqual(response.status_code, 302)
            response = self.client.get('/guestbook/')
            self.assertEqual(response.status_code, 200)
            added += 1
            # make sure one was added
            self.assertEqual(len(response.context['guest_comments']), 3 + added)

    def test_guestbook_form_good(self):
        """
        Check the form directly for validation
        """
        for good in self.good:
            form = GuestbookForm(good)
            comment = form.save()
            self.assertTrue(form.is_valid())
            self.assertEqual(comment.email, good['email'])
            self.assertEqual(comment.name, good['name'])
            if 'comment' in good:
                self.assertEqual(comment.comment, good['comment'])
            else:
                self.assertFalse(comment.comment)

    bad = [
        {
            # empty
        },
        {
            'email': 'not-valid',
            'name': 'Who cares',
        },
        {
            'email': 'lookslike@an.eml',
        },
        {
            'name': 'No email',
        },
    ]

    def test_guestbook_entry_bad(self):
        """
        Now, check some bad ones
        """
        for bad in self.bad:
            form = GuestbookForm(bad)
            try:
                comment = form.save()
            except ValueError:
                pass
            finally:
                self.assertFalse(form.is_valid())

    comments = [
        { # contains spam, should not validate
            'email': 'test@test.me',
            'name': 'Some Dude',
            'comment': 'EARN $$$ NOW! Just call me at 555 5555 5555!'
        },
        { # does not contain spam
            'email': 'bad@manners.always',
            'name': 'Bad Manners',
            'comment': 'Surprisingly, this should pass...'
        },
        { # contains spam, will validate but will be hidden
            'email': 'dear@friend.net',
            'name': 'Dear Friend',
            'comment': 'Dear Friend, if you would like to take up our offer right now, call on 555 5555 5555'
        }
    ]

    def test_bad_words(self):
        """
        Check comment validation for bad words
        Expected: 1=passes (but hidden), 2=passes, 3=fails
        """
        for index, comment in enumerate(self.comments):
            form = GuestbookForm(comment)
            try:
                result = form.save()
                self.assertTrue(index!=0 or result.hidden, msg='Comment not hidden when it should be')
                continue
            except ValueError:
                pass
            self.assertNotEqual(index, 1, msg='Comment does not validate when it should')
