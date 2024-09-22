from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import PostViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

from django.urls import path
from .views import UserFeedView

urlpatterns = [
    path('feed/', UserFeedView.as_view(), name='user-feed'),
]

from django.urls import path
from .views import like_post, unlike_post

urlpatterns = [
    path('posts/<int:pk>/like/', like_post, name='like_post'),
    path('posts/<int:pk>/unlike/', unlike_post, name='unlike_post'),
]
