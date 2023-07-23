from django_filters.rest_framework import DjangoFilterBackend
from dry_rest_permissions.generics import DRYPermissions
from rest_framework import viewsets

from .models import (
    CoffeeLog,
    CoffeeType,
    Goal,
    MentalHealth,
    MentalHealthLog,
    Milestone,
    MilestoneRoutineActivityRequirement,
    RoutineActivity,
    RoutineActivityLog,
)
from .serializers import (
    CoffeeLogSerializer,
    CoffeeTypeSerializer,
    GoalSerializer,
    MentalHealthLogSerializer,
    MentalHealthSerializer,
    MilestoneRoutineActivityRequirementSerializer,
    MilestoneSerializer,
    RoutineActivityLogSerializer,
    RoutineActivitySerializer,
)


class CoffeeLogViewSet(viewsets.ModelViewSet):
    queryset = CoffeeLog.objects.all()
    serializer_class = CoffeeLogSerializer
    permission_classes = (DRYPermissions,)


class CoffeeTypeViewSet(viewsets.ModelViewSet):
    queryset = CoffeeType.objects.all()
    serializer_class = CoffeeTypeSerializer
    permission_classes = (DRYPermissions,)


class GoalViewSet(viewsets.ModelViewSet):
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer
    permission_classes = (DRYPermissions,)
    filter_backend = [DjangoFilterBackend]
    filterset_fields = {
        "label": ["icontains"],
    }


class MentalHealthViewSet(viewsets.ModelViewSet):
    queryset = MentalHealth.objects.all()
    serializer_class = MentalHealthSerializer
    permission_classes = (DRYPermissions,)
    filter_backend = [DjangoFilterBackend]
    filterset_fields = {
        "label": ["icontains"],
    }


class MentalHealthLogViewSet(viewsets.ModelViewSet):
    queryset = MentalHealthLog.objects.all()
    serializer_class = MentalHealthLogSerializer
    permission_classes = (DRYPermissions,)


class MilestoneViewSet(viewsets.ModelViewSet):
    queryset = Milestone.objects.all()
    serializer_class = MilestoneSerializer
    permission_classes = (DRYPermissions,)
    filter_backend = [DjangoFilterBackend]
    filterset_fields = {
        "label": ["icontains"],
    }


class MilestoneRoutineActivityRequirementViewSet(viewsets.ModelViewSet):
    queryset = MilestoneRoutineActivityRequirement.objects.all()
    serializer_class = MilestoneRoutineActivityRequirementSerializer
    permission_classes = (DRYPermissions,)
    filter_backend = [DjangoFilterBackend]
    filterset_fields = {
        "completed_by_activity": ["exact"],
    }


class RoutineActivityViewSet(viewsets.ModelViewSet):
    queryset = RoutineActivity.objects.all()
    serializer_class = RoutineActivitySerializer
    permission_classes = (DRYPermissions,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class RoutineActivityLogViewSet(viewsets.ModelViewSet):
    queryset = RoutineActivityLog.objects.all()
    serializer_class = RoutineActivityLogSerializer
    permission_classes = (DRYPermissions,)
