from django import forms

from .models import GuestComment


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

