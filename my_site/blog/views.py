from datetime import date

from django.shortcuts import render


all_posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "Mount-Kinabalu.jpeg",
        "author": "Ricky",
        "date": date(2021, 7, 3),
        "title": "Mountain Hiking",
        "excerpt": "There's nothing like the views you get when hiking.",
        "content": '''
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Molestiae 
            at ipsa nisi veritatis id! Delectus assumenda iure quod doloremque, 
            deleniti odit dicta voluptate repellendus! Iusto voluptatem officia 
            quidem nemo sit.

            Lorem ipsum dolor sit amet consectetur adipisicing elit. Molestiae 
            at ipsa nisi veritatis id! Delectus assumenda iure quod doloremque, 
            deleniti odit dicta voluptate repellendus! Iusto voluptatem officia 
            quidem nemo sit.
        '''
    },
    {
        "slug": "this-is-post2",
        "image": "Mount-Kinabalu.jpeg",
        "author": "Ricky",
        "date": date(2021, 1, 13),
        "title": "Post2 title",
        "excerpt": "This is excerpt for post 2.",
        "content": '''
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Molestiae 
            at ipsa nisi veritatis id! Delectus assumenda iure quod doloremque, 
            deleniti odit dicta voluptate repellendus! Iusto voluptatem officia 
            quidem nemo sit.

            Lorem ipsum dolor sit amet consectetur adipisicing elit. Molestiae 
            at ipsa nisi veritatis id! Delectus assumenda iure quod doloremque, 
            deleniti odit dicta voluptate repellendus! Iusto voluptatem officia 
            quidem nemo sit.
        '''
    },
    {
        "slug": "this-is-post3",
        "image": "Mount-Kinabalu.jpeg",
        "author": "Ricky",
        "date": date(2021, 5, 28),
        "title": "Post3 title",
        "excerpt": "This is excerpt for post 3.",
        "content": '''
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Molestiae 
            at ipsa nisi veritatis id! Delectus assumenda iure quod doloremque, 
            deleniti odit dicta voluptate repellendus! Iusto voluptatem officia 
            quidem nemo sit.

            Lorem ipsum dolor sit amet consectetur adipisicing elit. Molestiae 
            at ipsa nisi veritatis id! Delectus assumenda iure quod doloremque, 
            deleniti odit dicta voluptate repellendus! Iusto voluptatem officia 
            quidem nemo sit.
        '''
    }
]


def get_date(post):
    return post['date']

# Create your views here.


def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, 'blog/index.html', {
        "posts": latest_posts
    })


def posts(request):
    return render(request, 'blog/all-posts.html', {
        "all_posts": all_posts
    })


def post_detail(request, slug):
    matching_post = next(post for post in all_posts if post["slug"] == slug)
    return render(request, 'blog/post-detail.html', {
        "post": matching_post
    })
