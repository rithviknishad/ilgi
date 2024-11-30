from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from ilgi.energy_journal.api.serializers.energy_log import EnergyLogSerializer
from ilgi.energy_journal.models import EnergyLog


class EnergyLogViewSet(ModelViewSet):
    serializer_class = EnergyLogSerializer
    queryset = EnergyLog.objects.select_related("created_by")
    lookup_field = "external_id"
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return super().get_queryset().filter(created_by=self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
