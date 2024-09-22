from django.db import models
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class Notification(models.Model):
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='notifications', on_delete=models.CASCADE)
    actor = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='actor', on_delete=models.CASCADE)
    verb = models.CharField(max_length=255)  # A short description of the action
    target_content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, blank=True, null=True)
    target_object_id = models.PositiveIntegerField(blank=True, null=True)
    target = GenericForeignKey('target_content_type', 'target_object_id')
    timestamp = models.DateTimeField(auto_now_add=True)  # Time of the notification
    read = models.BooleanField(default=False)  # To track if the notification has been read

    def __str__(self):
        return f'{self.actor} {self.verb} {self.target}'
