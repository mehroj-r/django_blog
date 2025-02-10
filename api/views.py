from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from myblog.models import Post
from .serializers import PostSerializer


class PostListView(APIView):
    """Handles listing and creating posts"""

    def get(self, request):

        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)

        return Response(serializer.data)

    def post(self, request):

        serializer = PostSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDetailView(APIView):
    """Handles retrieving, updating, and deleting a post"""

    def get_object(self, post_id):
        try:
            return Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return None

    def get(self, request, post_id):

        post = self.get_object(post_id)

        if not post:
            return Response({"error": "Post not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = PostSerializer(post)
        return Response(serializer.data, status = status.HTTP_200_OK)

    def put(self, request, post_id):

        post = self.get_object(post_id)

        if not post:
            return Response({"error": "Post not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = PostSerializer(post, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, post_id):

        post = self.get_object(post_id)

        if not post:
            return Response({"error": "Post not found"}, status=status.HTTP_404_NOT_FOUND)

        post.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class LatestPostsView(generics.ListAPIView):
    """Handles fetching the latest 3 posts"""
    queryset = Post.objects.all()[:3]
    serializer_class = PostSerializer
