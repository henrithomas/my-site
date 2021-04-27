from django.shortcuts import render
from django.http import HttpResponseNotFound, Http404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from .models import Post
from django.contrib import messages
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView)
from .blog_service import BlogService as bs


class PostsMonthView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<view_type>.html
    context_object_name = 'posts'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(date_posted__month=self.kwargs['month']) \
            .only('author', 'date_posted', 'title', 'content_display', 'id', 'slug') \
            .order_by('-date_posted')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home'
        return context

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<view_type>.html
    context_object_name = 'posts'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.all() \
            .only('author', 'date_posted', 'title', 'content_display', 'id', 'slug') \
            .order_by('-date_posted')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home'
        return context


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    query_pk_and_slug = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.title
        return context

class PostCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'content_display', 'slug']
    success_message = 'You can now view your post below...'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Write a Post'
        return context


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'content_display', 'slug']
    success_message = 'Your post has been updated.'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update'
        return context


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_message = 'Your post has been deleted.'
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Delete'
        return context


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


def home(request):
    context = {
        'posts': Post.objects
            .all()
            .only('author', 'date_posted', 'title', 'content_display', 'id', 'slug'),
        'title': 'Home'
    }
    return render(request, 'blog/home.html', context)


def single_post(request, slug):
    context = bs.get_single_post(slug)
    return render(request, 'blog/post_detail.html', context)

