from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView
from django.views import View

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


class SinglePostView(View):

    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        context = {
            'post': post,
            'post_tags': post.tags.all(),
            'comment_form': CommentForm(),
            'comments': post.comments.all().order_by('-id')
        }
        return render(request, 'blog/post-detail.html', context)

    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)  # creates a model instance but doesn't write to db yet
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse('post-detail-page', 
                args=[slug]))

        context = {
            'post': post,
            'post_tags': post.tags.all(),
            'comment_form': CommentForm(request.POST),
            'comments': post.comments.all().order_by('-id')
        }
        return render(request, 'blog/post-detail.html', context)


class ReadLaterView(View):
    def post(self, request):
        pass