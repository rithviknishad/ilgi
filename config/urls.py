from django.urls import include, path
from config import api_router
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

urlpatterns = [
    # Docs
    path("docs/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "docs/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path("docs/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    # API
    path("api/", include("openapi.urls")),
    path("api/auth/", include("users.urls")),
    path("api/", include(api_router.urlpatterns)),
]
