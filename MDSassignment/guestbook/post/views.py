from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Post 
from .forms import PostForm
import time
from django.utils import timezone

# Create your views here.
def post_page(request):
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			posts = Post()
			posts.name = form.cleaned_data['name']
			posts.text = form.cleaned_data['text']
			posts.email = form.cleaned_data['email']
			posts.save()
			messages.success(request, 'Thank you for posting.')
			return redirect('post_page')
	else:
		form = PostForm()

	posts = Post.objects.filter(status='p').order_by('-time')
	tally = Post.objects.filter(status='p').count()
	return render(request, 'post/post_page.html', {
		'posts':posts,
		'form': form,
		'tally' : tally,

		})

