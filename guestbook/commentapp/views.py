from django.shortcuts import render
from django.utils import timezone
from django.views.generic import CreateView
from django.core.urlresolvers import reverse
from datetime import timedelta

from .models import GuestPost
from .forms import GuestPostForm

# Create your views here.
class GuestPostsCreateView(CreateView):
    model = GuestPost
    template_name = 'post.html'
    form_class = GuestPostForm

    def get_success_url(self):
        return reverse('thank-you')

    def convert_date(self, pub_date):
        diff = timezone.now() - pub_date
        day = timedelta(hours=24)
        days_elapsed = int(diff.total_seconds() / day.total_seconds())
        if diff.total_seconds() <= 10:
            return "Just now"
        elif days_elapsed == 0:
            return "Today"
        elif days_elapsed == 1:
            return "Yesterday"
        else:
            return "{} days ago".format(days_elapsed)

    def get_context_data(self, **kwargs):
        context = super(GuestPostsCreateView, self).get_context_data(**kwargs)
        # output should be in chronological order
        guestposts = self.model.objects.order_by('-pub_date').filter(show=True)
        for post in guestposts:
            post.pub_date = self.convert_date(post.pub_date)
        context['postlist'] = guestposts
        # number of guests posted on the guest book, include only shown entries
        context['guestcount'] = self.model.objects.filter(show=True).count() 
        return context

