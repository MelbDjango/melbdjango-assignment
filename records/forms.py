from django import forms
from django.utils import timezone


from .models import Record

class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields=('name','comment','email_address')

    # Double check email confirmation
    confirm_email = forms.CharField(max_length=200)

    def clean_comment(self):
        comment = self.cleaned_data['comment']
      
        if comment == 'test':
            msg = 'This is not for testing'
            self.add_error('comment', msg)

        return comment

    def clean(self):
        cleaned_data = super(RecordForm, self).clean()
        
        email_address = self.cleaned_data.get('email_address')
        confirm_email = self.cleaned_data.get('confirm_email')
        entry_date = self.cleaned_data.get('entry_date')
        
        if email_address and confirm_email:
            if email_address != confirm_email:
                msg = 'Email doesn\'t match'
                self.add_error('email_address', msg)
                self.add_error('confirm_email', msg)
            else:
                entry_date = timezone.now()
      




        




    



