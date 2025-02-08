from django.shortcuts import render
from myblog.models import Post
from . import utils

def index(request):
    posts = utils.getPosts()
    return render(request, 'index.html', {'posts':posts})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def postID(request, id):
    post = utils.getPost(id)
    return render(request, 'post.html', {'post':post})