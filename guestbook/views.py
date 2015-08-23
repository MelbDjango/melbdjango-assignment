from django.core.urlresolvers import reverse_lazy

# Create your views here.
from django.views.generic import CreateView, RedirectView

from .forms import GuestbookForm
from .models import GuestComment


class Guestbook(CreateView):
    model = GuestComment
    template_name = 'guestbook.html'
    form_class = GuestbookForm
    success_url = reverse_lazy('guestbook')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['guest_comments'] = self.model.objects.filter(hidden=False).order_by('-entrydate')
        context['entries'] = self.model.objects.count()
        return context


class RootRedirectView(RedirectView):
    permanent = False
    url = reverse_lazy('guestbook')

