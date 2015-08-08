from django import forms

class EntryForm(forms.Form):
    fname = forms.CharField(max_length=50, label='First name')
    lname = forms.CharField(max_length=50, label='Last name', required=False)
    email = forms.EmailField(required=False)
    comment = forms.CharField(max_length=500)
