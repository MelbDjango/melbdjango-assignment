from django.views.generic import CreateView, RedirectView
from django.core.urlresolvers import reverse
from django.http import Http404

from .models import Record
from .forms import RecordForm


class RecordCreateView(CreateView):
    model = Record
    template_name = 'records.html'
    form_class = RecordForm
    context_object_name = 'record_form'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(RecordCreateView, self).get_context_data(**kwargs)
        context['record_form'] = self.model.objects.all()
        return context