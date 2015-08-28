import re
from django import forms
from django.forms import Textarea
from django.utils import timezone
from django.utils.safestring import mark_safe


from .models import Record

class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields=('first_name', 'last_name', 'comment', 'email_address')
        widgets = { 'comment': Textarea(attrs={'cols':35, 'rows':5}),}

    # Double check email confirmation
    confirm_email = forms.EmailField(required=False)

    def clean_comment(self): 
        comment = self.cleaned_data['comment']     
        filter_list = ['Lose weight','100% free','Dear Friend']
        reg = re.compile(r'([a-z])\1{10,}' + '|' + '|'.join(filter_list), re.IGNORECASE)
        matched_value = ', '.join([str(m.group(0)) for m in reg.finditer(comment)])

        if matched_value:
            raise forms.ValidationError(mark_safe
                ('Laracroft hate spams, please try again:<br />' + 
                    matched_value))

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
      




        




    



