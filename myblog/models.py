from django.db import models

class Post(models.Model):

    # Main Properties
    title = models.CharField(max_length=100)
    description = models.TextField()
    content = models.TextField()
    author = models.CharField(max_length=100)
    thumbnail = models.CharField()

    # Timing Properties
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)