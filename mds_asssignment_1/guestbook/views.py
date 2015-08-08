from django.shortcuts import render

from .models import Entry

def home(request):
    return entries(request)

def entries(request):
    entry_list = Entry.objects.all()
    return render(request, 'entries.html', {
        'entry_list': entry_list,
    })
