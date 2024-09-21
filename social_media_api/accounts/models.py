from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    # Define a ManyToMany relationship for following, using an intermediate model
    following = models.ManyToManyField(
        'self', 
        through='UserFollowing', 
        through_fields=('follower', 'following'),  # Use follower and following to remove ambiguity
        symmetrical=False, 
        related_name='followers'  # users who are following this user
    )

    # Avoid clashes with the built-in User model by using custom related_names for groups and permissions
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',  # Custom related_name to avoid clashes
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions_set',  # Custom related_name to avoid clashes
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def __str__(self):
        return self.username


class UserFollowing(models.Model):
    follower = models.ForeignKey(CustomUser, related_name='user_follows', on_delete=models.CASCADE)
    following = models.ForeignKey(CustomUser, related_name='user_followed_by', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('follower', 'following')  # Prevent a user from following the same person twice

    def __str__(self):
        return f"{self.follower.username} follows {self.following.username}"
