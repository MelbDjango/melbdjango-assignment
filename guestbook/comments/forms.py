from django import forms

from .models import Comment, Message

class CreateCommentForm(forms.ModelForm):
    text = forms.CharField(
        label="Comment",
        max_length=1024,
        widget=forms.Textarea)

    class Meta:
        model = Comment
        fields = ('title', 'text', 'is_public')

class AddMessageForm(forms.ModelForm):

    class Meta:
        model = Message
        fields = ('text',)
