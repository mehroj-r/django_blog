from django.db import models

class Post(models.Model):

    title = models.CharField(max_length=100)
    description = models.TextField()
    content = models.TextField()
    author = models.CharField(max_length=100)
    thumbnail = models.CharField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):

    content = models.TextField()
    author = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)