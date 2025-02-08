from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from myblog.models import Post
from .serializers import PostSerializer

@api_view(['GET'])
def getPosts(request):

    posts = Post.objects.all()[:3]
    serializer = PostSerializer(posts, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def getAllPosts(request):

    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)

    return Response(serializer.data)

@api_view(['POST'])
def createPost(request):

    serializer = PostSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getPost(request, id):

    post = Post.objects.get(id=id)
    serializer = PostSerializer(post)

    return Response(serializer.data)

@api_view(['PUT'])
def updatePost(request, id):
    post = Post.objects.get(id=id)

    serializer = PostSerializer(post, data=request.data)
    if serializer.is_valid():
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def deletePost(request, id):

    post = Post.objects.get(id=id)
    post.delete()

    return Response(status=status.HTTP_204_NO_CONTENT)