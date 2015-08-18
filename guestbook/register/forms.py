from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import validate_email



class ValidUniqueUserEmailField(forms.EmailField):
    def validate(self, value):
        super(forms.EmailField, self).validate(value)

        print(type(value))

        if value != '':

            try:
                validate_email(value)
            except:
                raise forms.ValidationError("Please enter a valid email")

            try:
                User.objects.get(email=value)
                raise forms.ValidationError("Email already exists")
            except User.MultipleObjectsReturned:
                raise forms.ValidationError("Email already exists")
            except User.DoesNotExist:
                pass


class UserCreateForm(UserCreationForm):
    email = ValidUniqueUserEmailField(required=False, label='Email (Optional):')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')



    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
