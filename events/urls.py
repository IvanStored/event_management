from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventViewSet

router = DefaultRouter()
router.register(r"events_list", EventViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
