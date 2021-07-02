from django.http import response
from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import Http404

posts = [
    {"username": "user1", "title": "post1", "content": "post 1 text"},
    {"username": "user2", "title": "post2", "content": "post 2 text"},
    {"username": "user3", "title": "post3", "content": "post 3 text"},
]


# Create your views here.
def index(request):
    return render(request, "blog/index.html")


def all_posts(request):
    return render(request, 'blog/posts.html', {
        "posts": posts
    })


def post(request, title):
    try:
        for post in posts:
            if post['title'] == title:
                context = {
                    "username": post['username'],
                    "title": post['title'],
                    "content": post['content']
                }
                return render(request, "blog/post.html", context)
    except:
        raise Http404()