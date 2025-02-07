from django.shortcuts import render

from myblog.models import Post


def index(request):

    posts = Post.objects.all()
    for post in posts:
        print(post.title)

    return render(request, 'index.html', {'posts':posts})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def post(request):
    return render(request, 'post.html')


def postID(request, id):
    postByID = Post.objects.get(id=id)
    return render(request, 'post.html', {'post':postByID})