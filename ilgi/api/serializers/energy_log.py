from ilgi.models import EnergyLog
from rest_framework.serializers import ModelSerializer
from users.serializers import UserSerializer
from rest_framework import serializers


class EnergyLogSerializer(ModelSerializer):
    id = serializers.UUIDField(read_only=True, source="external_id")
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = EnergyLog
        read_only_fields = (
            "created_by",
            "created_at",
            "updated_at",
        )
        exclude = (
            "external_id",
            "deleted",
        )
