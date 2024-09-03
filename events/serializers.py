from rest_framework import serializers
from .models import Event, EventRegistration


class EventRegistrationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True)
    email = serializers.EmailField(source="user.email", read_only=True)

    class Meta:
        model = EventRegistration
        fields = ("username", "email")


class EventSerializer(serializers.ModelSerializer):
    organizer = serializers.SlugRelatedField(
        many=False, read_only=True, slug_field="username"
    )
    participants = EventRegistrationSerializer(
        many=True, read_only=True, source="registrations"
    )

    class Meta:
        model = Event
        fields = "__all__"
