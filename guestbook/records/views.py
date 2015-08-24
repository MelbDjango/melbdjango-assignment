from django.views.generic import CreateView, RedirectView
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import Http404

from .models import Record
from .forms import RecordForm

class RecordCreateView(CreateView):
    model = Record
    template_name = 'records.html'
    form_class = RecordForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(RecordCreateView, self).get_context_data(**kwargs)
        context['record_list'] = self.model.objects.all()
        return context
