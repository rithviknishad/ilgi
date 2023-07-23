from rest_framework import routers

from .views import UserViewSet

users_router = routers.SimpleRouter()
users_router.register(r"users/user", UserViewSet)
