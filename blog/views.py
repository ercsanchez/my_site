from django.forms.widgets import SplitDateTimeWidget
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
            # creates a model instance but doesn't write to db yet
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse('post-detail-page', args=[slug]))

        context = {
            'post': post,
            'post_tags': post.tags.all(),
            'comment_form': CommentForm(request.POST),
            'comments': post.comments.all().order_by('-id')
        }
        return render(request, 'blog/post-detail.html', context)


class ReadLaterView(View):
    def get(self, request):
        stored_posts = request.session.get('stored_posts')
        context = {}

        if stored_posts is None or len(stored_posts) == 0:
            context['posts'] = []
            context['has_posts'] = False
        else:
            context['posts'] = Post.objects.filter(id__in=stored_posts)
            context['has_posts'] = True

        return render(request, 'blog/stored-posts.html', context)

    def post(self, request):
        stored_posts = request.session.get('stored_posts')

        if stored_posts is None:
            stored_posts = []

        post_id = int(request.POST['post_id'])

        if post_id not in stored_posts:
            stored_posts.append(post_id)
            request.session['stored_posts'] = stored_posts

        return HttpResponseRedirect('/')
