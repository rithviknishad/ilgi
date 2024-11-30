from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import views
from drf_spectacular.utils import extend_schema

# Create decorated views with tags
TokenObtainPairView = extend_schema(
    summary="Get JWT tokens for authentication",
    description="Returns the JWT tokens for authentication",
    tags=['Authentication']
)(TokenObtainPairView)
TokenRefreshView = extend_schema(
    summary="Refresh JWT tokens",
    description="Returns the refreshed JWT tokens",
    tags=['Authentication']
)(TokenRefreshView)

app_name = 'users'

urlpatterns = [
    path('me/', views.UserMeView.as_view(), name='user-me'),
    path('token/', TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('token/refresh/', TokenRefreshView.as_view(), name="token_refresh"),
]
