from django.shortcuts import render, redirect
from .models import Post 
from .forms import PostForm

# Create your views here.
def post_page(request):
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			posts = Post()
			#there is a problem here - form has no attribute 'name'
			posts.name = form.cleaned_data['name']
			posts.text = form.cleaned_data['text']
			posts.email = form.cleaned_data['email']
			#posts.time = form.cleaned_data['time']
			posts.save()
			return redirect('post_page')
	else:
		form = PostForm()

	posts = Post.objects.all().order_by('time')
	tally = Post.objects.count()
	return render(request, 'post/post_page.html', {
		'posts':posts,
		'form': form,
		'tally' : tally,

		})

