from django.db import models
from django.db.models import ManyToManyField

from user.models import CustomUser

class EventType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Event(models.Model):
    title = models.CharField(max_length=100)
    event_type = models.ForeignKey(
        EventType, on_delete=models.CASCADE, related_name="events", default=""
    )
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=100)
    organizer = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="organized_events"
    )

    def __str__(self):
        return self.title


class EventRegistration(models.Model):
    event = models.ForeignKey(
        Event, on_delete=models.CASCADE, related_name="registrations"
    )
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("event", "user")
