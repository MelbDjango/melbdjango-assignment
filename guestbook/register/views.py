from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from .forms import UserCreateForm


def register(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            new_user = authenticate(username=request.POST['username'],
                                    password=request.POST['password1'])
            login(request, new_user)
            return redirect('home')
    else:
        form = UserCreateForm()
    context = dict(form=form)
    return render(request, 'register.html', context)
