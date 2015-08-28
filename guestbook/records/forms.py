from django import forms
from django.utils import timezone


from .models import Record

class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields=('name', 'comment', 'email_address')
