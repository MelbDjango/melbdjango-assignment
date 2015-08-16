from django import forms
from django.forms import ModelForm
from .models import Post


class PostForm(forms.ModelForm):

	class Meta:
		model = Post
		fields = ['name', 'text', 'email']


	def clean_text(self):
		text = self.cleaned_data.get('text')
		if text.lower() == "lose weight":
			raise forms.ValidationError("fail: spam")
		if text.lower() == "100% free":
			raise forms.ValidationError("fail: spam")
		if text.lower() == "dear friend":
			raise forms.ValidationError("fail: spam")
		return text




