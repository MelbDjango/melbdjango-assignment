from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin
from django.views.generic import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.utils import timezone

from .models import Comment, Message
from .forms import AddMessageForm, CreateCommentForm


class AllCommentList(SuccessMessageMixin, CreateView):
    model = Comment
    template_name = 'public_comments_list.html'
    form_class = AddMessageForm
    context_object_name = 'comments'
    success_message = "Message was created successfully"

    def form_valid(self, form):
        comment_id = self.request.POST['comment_id']
        form.instance.user = self.request.user
        form.instance.comment = Comment.objects.get(pk=comment_id)
        return super(AllCommentList, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(AllCommentList, self).get_context_data(**kwargs)
        context['comments'] = self.model.objects.filter(is_active=True).filter(is_public=True)

        return context

    def get_success_url(self):
        return reverse_lazy('all_comments_list')


class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)

class UserCommentList(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = 'comments_list.html'
    form_class = CreateCommentForm
    context_object_name = 'comments'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(UserCommentList, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('user_comments_list')

    def get_context_data(self, **kwargs):
        context = super(UserCommentList, self).get_context_data(**kwargs)
        context['comments'] = self.model.objects.filter(is_active=True).filter(author=self.request.user.pk)
        return context


class UserCommentDetail(LoginRequiredMixin, DetailView):
    model = Comment
    template_name = 'comments_detail.html'

class UserCommentCreate(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = 'comments_form.html'
    form_class = CreateCommentForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(UserCommentCreate, self).form_valid(form)

class UserCommentUpdate(LoginRequiredMixin, UpdateView):
    model = Comment
    template_name = 'comments_form.html'
    success_url = reverse_lazy('user_comments_list')
    fields = ['title', 'text', 'created_at', 'is_public', 'is_active']

    ## Todo - makesure user is author

class UserCommentDelete(LoginRequiredMixin, DeleteView):
    model = Comment
    template_name = 'comments_confirm_delete.html'
    success_url = reverse_lazy('user_comments_list')

    ## Todo - change delete to update 'is_active' to False

    ## Todo - makesure user is author
