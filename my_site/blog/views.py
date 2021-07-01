from django.shortcuts import render

posts = [
    {"user": "user1", "title": "post1", "text": "post 1 text here"},
    {"user": "user2", "title": "post2", "text": "post 2 text here"},
    {"user": "user3", "title": "post3", "text": "post 3 text here"},
]


# Create your views here.
def index(request):
    return render(request, "blog/index.html", )