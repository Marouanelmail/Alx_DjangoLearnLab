from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    actor = serializers.StringRelatedField()  # To show the actor's username
    target = serializers.StringRelatedField()  # Show the target of the notification

    class Meta:
        model = Notification
        fields = ['actor', 'verb', 'target', 'timestamp', 'read']
