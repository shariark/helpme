from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
from django.http import HttpResponse
from django.views.generic import ListView, TemplateView, DetailView, UpdateView, DeleteView
from .models import statuscategory
from .models import statusdescription
from post.models import post
from post.models import comment
from django.views import generic
from django.urls import reverse_lazy
from .forms import edit_post



class home(ListView):
    template_name = "index.html"
    model = post
    ordering = ['-id']

    def get_queryset(self):
        query_set = super().get_queryset()
        return query_set.select_related
        ('statuscategory')


def setting(request):
    return render(request, 'setting.html')


def signup(request):
    return render(request, 'signup.html')


class comments(generic.DetailView):
    model = post
    template_name = 'comment.html'
    ordering = ['-id']

    def get_context_data(self, *args, **kwargs):
        context = super(comments, self).get_context_data(*args, **kwargs)
        context['comment_list'] = comment.objects.all()
        return context


class edit(UpdateView):
    model=post
    form_class=edit_post
    template_name = 'edit.html'
    



class delete(DeleteView):
    model = post
    template_name = 'delete.html'
    fields = ['status']
    success_url = reverse_lazy('profile')


def search(request):
    search = request.GET['search']
    if len(search) > 81:
        allpost = post.objects.none()
    elif len(search) < 1:
        allpost = post.objects.none()
    else:
        allpoststatus = post.objects.filter(status__icontains=search)
        allpostauthor_name = post.objects.filter(author_name__icontains=search)
        allpost=allpoststatus.union(allpostauthor_name)
    params = {'allpost': allpost, 'search': search}
    return render(request, 'search.html', params)
