from django.forms import ModelForm, Textarea, ValidationError

from .models import Post

SPAM_MESSAGE = 'No spam please.'


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['name', 'text', 'email']
        widgets = {
            'text': Textarea(attrs={'cols': 80, 'rows': 5}),
        }

    def clean_name(self):
        return self.check_spam(self.cleaned_data['name'])

    def clean_text(self):
        return self.check_spam(self.cleaned_data['text'])

    def check_spam(self, data):
        if is_spam(data):
            raise ValidationError(SPAM_MESSAGE)
        return data


def is_spam(text):
    """
    Checks to see if the given text is spam by checking whether it contains
    common spam phrases. This seems like a poor approach!
    """
    spam_phrases = ('dear friend', 'lose weight', '100% free', )
    text = text.lower()
    for phrase in spam_phrases:
        if text.find(phrase) >= 0:
            return True

    return False
