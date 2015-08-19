from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy

from .models import Post
from .forms import PostForm


class PostCreateList(CreateView):
    """
    A view to create and list posts.

    This is achieved by using a create view
    and adding our list of posts to the context.
    """
    form_class = PostForm
    model = Post
    template_name = 'guestbook/guestbook.html'
    success_url = reverse_lazy('guestbook:post-create-list')

    def get_context_data(self, **kwargs):
        # we override get_context_data here to add our list of posts to the
        # context so we can show the form and the list of posts on the one page

        post_list = get_valid_posts()
        kwargs['post_list'] = post_list
        kwargs['post_count'] = len(post_list)
        return super().get_context_data(**kwargs)


def get_valid_posts():
    """
    Returns a queryset of non-hidden posts.
    """
    return Post.objects.filter(hidden_at=None)
