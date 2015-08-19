from django.db import models


class Post(models.Model):
    """
    Model representing a single post in the guestbook.
    The post consists of
        - the name of the person
        - a comment
        - a contact email
        - the timestamp of when the post was created
        - the timestamp of when the post was hidden (if at all)
    """
    name = models.CharField(max_length=254)
    text = models.CharField(max_length=1000)
    email = models.EmailField(blank=True)
    created_at = models.DateTimeField(auto_now=True)
    hidden_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ('-created_at', )

    def __str__(self):
        text = self.text
        if len(self.text) > 30:
            text = self.text[:30]

        return (
            'Post created: {}, name: {}, text: {}'
            ''.format(self.created_at.isoformat(),
                      self.name,
                      text)
        )
