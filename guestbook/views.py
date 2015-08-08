from django import forms
from django.contrib import messages
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.decorators.http import require_http_methods

from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email_address', 'comment')

@require_http_methods(('GET', 'POST'))
def mypage(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Thank you for your comment.')

            return HttpResponseRedirect(reverse('mypage'))
        else:
            # Didn't validate
            messages.info(request, "Hmm, seems there's a problem with your comment.")
    else:
        # GET
        form = CommentForm()

    comments_for_page = Comment.objects.exclude(hide=True).order_by('-created')

    return render(request, 'mypage.html', {'comments': comments_for_page, 'form': form})

@require_http_methods(('GET', 'POST'))
def backend(request):
    assert False, "Not yet implemented"
