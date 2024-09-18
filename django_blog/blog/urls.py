from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Your other URL patterns
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
