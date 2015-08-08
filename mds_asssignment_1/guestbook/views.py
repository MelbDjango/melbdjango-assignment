from django.shortcuts import render

from .forms import EntryForm
from .models import Entry

import datetime


def home(request):
    if request.method == 'POST':
        entry_form = EntryForm(request.POST)
        if entry_form.is_valid():
            # do something
            entry = Entry()
            entry.fname = entry_form.cleaned_data['fname']
            entry.lname = entry_form.cleaned_data['lname']
            entry.email = entry_form.cleaned_data['email']
            entry.comment = entry_form.cleaned_data['comment']
            entry.visible = True
            entry.date = datetime.datetime.now()
            entry.save()

    else:
        entry_form = EntryForm()

    entry_list = Entry.objects.all().filter(visible=True).order_by('date').reverse()
    return render(request, 'entries.html', {
        'entry_list': entry_list,
        'entry_form': entry_form,
    })
