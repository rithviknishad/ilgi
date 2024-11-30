from django.conf import settings
from django.urls import include, path
from rest_framework.routers import DefaultRouter, SimpleRouter
from ilgi.api.viewsets.energy_log import EnergyLogViewSet

router = DefaultRouter() if settings.DEBUG else SimpleRouter()

router.register(r"energy-logs", EnergyLogViewSet, basename="energy-logs")

app_name = "api"
urlpatterns = [
    path("", include(router.urls)),
]
