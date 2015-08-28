from django.views.generic import (
    RedirectView, ListView, DetailView, CreateView, UpdateView, TemplateView )
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import Http404

from .models import Record
from .forms import RecordForm


class RecordCreateView(CreateView):
    model = Record
    template_name = 'records.html'
    form_class = RecordForm
    success_url = reverse_lazy('thank-you')

    def get_context_data(self, **kwargs):
        context = super(RecordCreateView, self).get_context_data(**kwargs)
        context['record_list'] = Record.objects.all().order_by('-entry_date')
        return context


class RecordDetailView(DetailView):
    model = Record
    template_name = 'record_detail.html'

    def get_context_data(self, **kwargs):
         context = super(RecordDetailView, self).get_context_data(**kwargs)
         context['record_detail'] = Record.objects.all()
         return context

class RecordThanksView(TemplateView):
    template_name = 'thank_you.html'

class RecordRedirectView(RedirectView):
    permanent = False
    url = reverse_lazy('record-list')


