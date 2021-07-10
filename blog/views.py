from blog.forms import CommentForm
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Post
from .forms import CommentForm

# Create your views here.


class StartingPageView(ListView):
    model = Post
    template_name = 'blog/index.html'
    ordering = ['-date']
    context_object_name = 'posts'

    def get_queryset(self):
        return super().get_queryset()[:3]


class AllPostsView(ListView):
    model = Post
    template_name = 'blog/all-posts.html'
    ordering = ['-date']
    context_object_name = 'all_posts'


class SinglePostView(DetailView):
    model = Post
    template_name = 'blog/post-detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_tags'] = self.object.tags.all()
        context['comment_form'] = CommentForm()
        return context
