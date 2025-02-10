from rest_framework import serializers
from myblog.models import Post

class PostSerializer(serializers.ModelSerializer):

    created_at = serializers.DateTimeField(format="%I:%M %p, %b %d, %Y")

    class Meta:
        model = Post
        fields = '__all__'