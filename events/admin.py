from django.contrib import admin

from events.models import Event, EventRegistration, EventType

admin.site.register(Event)
admin.site.register(EventRegistration)
admin.site.register(EventType)
