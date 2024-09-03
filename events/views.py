from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Event, EventRegistration, EventType
from .serializers import EventSerializer, EventRegistrationSerializer
from .permissions import IsOrganizerOrReadOnly


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOrganizerOrReadOnly,
    ]

    def get_queryset(self):
        location = self.request.query_params.get("location")
        title = self.request.query_params.get("title")
        description = self.request.query_params.get("description")
        event_type = self.request.query_params.get("event_type")
        queryset = self.queryset

        if location:
            queryset = queryset.filter(location__contains=location)
        if title:
            queryset = queryset.filter(title__icontains=title)
        if description:
            queryset = queryset.filter(description__icontains=description)
        if event_type:
            queryset = queryset.filter(event_type__name__icontains=event_type)
        return queryset.all()

    def perform_create(self, serializer):
        event_type, created = EventType.objects.get_or_create(name=self.request.data.get("event_type"))
        serializer.save(organizer=self.request.user, event_type=event_type)

    def get_serializer_class(self):
        if self.action == "register_to_event":
            return EventRegistrationSerializer
        return EventSerializer

    @action(
        detail=True,
        methods=["post"],
        permission_classes=[permissions.IsAuthenticated],
    )
    def register_to_event(self, request, pk=None):
        event = self.get_object()
        registration, created = EventRegistration.objects.get_or_create(
            event=event, user=request.user
        )
        if not created:
            return Response(
                {"status": "You are already registered"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response(
            {"status": "Registration successful"},
            status=status.HTTP_201_CREATED,
        )

    @extend_schema(
        parameters=[
            OpenApiParameter(
                "location",
                type=OpenApiTypes.STR,
                description="Filter by location (ex. ?location=USA)",
            ),
            OpenApiParameter(
                "title",
                type=OpenApiTypes.STR,
                description="Filter by title (ex. ?title=medicine)",
            ),
            OpenApiParameter(
                "description",
                type=OpenApiTypes.STR,
                description="Filter by description (ex. ?description=medicine)",
            ),
            OpenApiParameter(
                "event_type",
                type=OpenApiTypes.STR,
                description="Filter by event type (ex. ?event_type=Conference)",
            ),
        ]
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
