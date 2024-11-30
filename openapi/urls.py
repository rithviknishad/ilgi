from django.views.generic import TemplateView
from django.urls import path
from rest_framework.schemas import get_schema_view

TITLE = "ilgi"
DESCRIPTION = """
Digital Journal
"""
VERSION = "1.0.0"


urlpatterns = [
    path(
        "schema/",
        get_schema_view(title=TITLE, description=DESCRIPTION, version=VERSION),
        name="openapi-schema",
    ),
    path(
        "swagger-ui/",
        TemplateView.as_view(
            template_name="openapi/swagger-ui.html",
            extra_context={"schema_url": "openapi-schema"},
        ),
        name="swagger-ui",
    ),
]
