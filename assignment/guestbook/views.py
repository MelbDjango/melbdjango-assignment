from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Post
from .forms import PostForm


class PostCreateList(SuccessMessageMixin, CreateView):
    """
    A view to create and list posts.

    This is achieved by using a create view
    and adding our list of posts to the context.
    """
    form_class = PostForm
    model = Post
    template_name = 'guestbook/guestbook.html'
    success_url = reverse_lazy('guestbook:post-create-list')
    success_message = 'Thanks for posting in the guestbook, %(name)s!'

    def get_context_data(self, **kwargs):
        # we override get_context_data here to add our list of posts to the
        # context so we can show the form and the list of posts on the one page

        post_list = get_valid_posts()
        paginator = Paginator(post_list, 5)
        page = self.request.GET.get('page')
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)

        kwargs['posts'] = posts
        kwargs['post_count'] = len(post_list)
        return super().get_context_data(**kwargs)


def get_valid_posts():
    """
    Returns a queryset of non-hidden posts.
    """
    return Post.objects.filter(hidden_at=None)
