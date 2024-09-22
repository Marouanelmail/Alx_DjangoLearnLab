from rest_framework import viewsets, permissions
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

from rest_framework import filters

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']  # Allow search by title and content

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

from rest_framework import generics
from .models import Post
from .serializers import PostSerializer
from rest_framework.permissions import IsAuthenticated

class UserFeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Get posts from users the current user follows
        user = self.request.user
        following_users = user.following.all()
        return Post.objects.filter(author__in=following_users).order_by('-created_at')

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post, Like
from notifications.models import Notification

@api_view(['POST'])
def like_post(request, pk):
    post = Post.objects.get(pk=pk)
    like, created = Like.objects.get_or_create(user=request.user, post=post)
    
    if created:
        Notification.objects.create(
            recipient=post.author, 
            actor=request.user, 
            verb='liked', 
            target=post
        )
        return Response({'message': 'Post liked.'}, status=status.HTTP_201_CREATED)
    else:
        return Response({'message': 'Already liked.'}, status=status.HTTP_200_OK)

@api_view(['POST'])
def unlike_post(request, pk):
    post = Post.objects.get(pk=pk)
    try:
        like = Like.objects.get(user=request.user, post=post)
        like.delete()
        return Response({'message': 'Post unliked.'}, status=status.HTTP_204_NO_CONTENT)
    except Like.DoesNotExist:
        return Response({'message': 'You haven\'t liked this post.'}, status=status.HTTP_400_BAD_REQUEST)

from rest_framework import generics
from .models import Notification
from .serializers import NotificationSerializer
from rest_framework.permissions import IsAuthenticated

class NotificationListView(generics.ListAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(recipient=self.request.user).order_by('-timestamp')

from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Post
from .serializers import PostSerializer
from notifications.models import Notification

@api_view(['POST'])
def like_post(request, pk):
    # Retrieve the post object using get_object_or_404
    post = generics.get_object_or_404(Post, pk=pk)
    
    # Check if the post is already liked by the user
    if post.likes.filter(id=request.user.id).exists():
        return Response({'message': 'You have already liked this post.'}, status=status.HTTP_400_BAD_REQUEST)
    
    # Add the like
    post.likes.add(request.user)
    
    # Create a notification for the post author
    Notification.objects.create(
        recipient=post.author,
        actor=request.user,
        verb='liked',
        target=post,
    )

    return Response({'message': 'Post liked successfully.'}, status=status.HTTP_200_OK)
