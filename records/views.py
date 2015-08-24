from django.views.generic import CreateView, RedirectView, DetailView
from django.core.urlresolvers import reverse
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
        context['record_list'] = Record.objects.all()
        return context


class RecordDetailView(DetailView):
    model = Record

    def get_context_data(self, **kwargs):
         context = super(RecordDetailView, self).get_context_data(**kwargs)
         context['record_detail'] = Record.objects.all()
         return context



