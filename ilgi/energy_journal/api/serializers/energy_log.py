from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from ilgi.energy_journal.models import EnergyLog
from ilgi.users.serializers import UserSerializer


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
