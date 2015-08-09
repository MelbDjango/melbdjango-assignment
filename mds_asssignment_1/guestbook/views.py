from django.shortcuts import render

from .forms import EntryForm
from .models import Entry


def home(request):
    entry_list = Entry.objects.all().filter(visible=True).order_by('date').reverse()
    if request.method == 'POST':
        entry_form = EntryForm(request.POST)
        if entry_form.is_valid():
            entry = Entry()
            entry.fname = entry_form.cleaned_data['fname']
            entry.lname = entry_form.cleaned_data['lname']
            entry.email = entry_form.cleaned_data['email']
            entry.comment = entry_form.cleaned_data['comment']
            entry.save()
            return render(request, 'entries.html', {
                'thankyou': entry.fname,
                'entry_list': entry_list,
            })

    else:
        entry_form = EntryForm()

    return render(request, 'entries.html', {
        'entry_list': entry_list,
        'entry_form': entry_form,
    })
