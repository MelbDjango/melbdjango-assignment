from django import forms
from django.core.exceptions import ValidationError

from .models import GuestComment, SpamWord


class GuestbookForm(forms.ModelForm):
    class Meta:
        model = GuestComment
        fields = ('email', 'name', 'comment')
        labels = {
            'email': 'Contact Email',
        }
        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your email address'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your name'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': '3', 'cols': '40',
                                             'placeholder': 'Enter an optional comment or simply leave blank'}),
        }

    def clean(self):
        """
        Spam/profanity validation
        Even though this validation done on the comment, we may need to toggle
        the 'hidden' attribute if the word is allowed but needs to be vetted
        """
        data = self.cleaned_data.get('comment')
        if data:
            data = data.lower()
            for word in SpamWord.objects.all():
                if word.spam.lower() in data:
                    if word.reject:
                        raise ValidationError('Disallowed word found in comment')
                    else:
                        # Just hide it
                        self.instance.hidden = True

