from rest_framework import serializers

from .models import (
    CoffeeLog,
    CoffeeType,
    Goal,
    Habit,
    HabitLog,
    MentalHealth,
    MentalHealthLog,
    Milestone,
    MilestoneHabitRequirement,
    MilestoneRoutineActivityRequirement,
    RoutineActivity,
    RoutineActivityLog,
)


class RoutineActivitySerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(source="external_id", read_only=True)

    class Meta:
        model = RoutineActivity
        exclude = (
            "deleted",
            "owner",
        )
        read_only_fields = (
            "external_id",
            "created_on",
            "modified_on",
            "discontinued_on",
        )


class RoutineActivityLogSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(source="external_id", read_only=True)

    class Meta:
        model = RoutineActivityLog
        exclude = ("deleted",)
        read_only_fields = (
            "external_id",
            "created_on",
            "modified_on",
            "routine",
        )


class HabitSeriaizer(serializers.ModelSerializer):
    id = serializers.UUIDField(source="external_id", read_only=True)

    class Meta:
        model = Habit
        exclude = (
            "deleted",
            "owner",
        )
        read_only_fields = (
            "external_id",
            "created_on",
            "modified_on",
            "discontinued_on",
        )


class HabitLogSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(source="external_id", read_only=True)

    class Meta:
        model = HabitLog
        exclude = ("deleted",)
        read_only_fields = (
            "external_id",
            "created_on",
            "modified_on",
            "habit",
        )


class CoffeeTypeSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(source="external_id", read_only=True)

    total_quantity = serializers.SerializerMethodField()
    total_price = serializers.SerializerMethodField()

    def get_total_quantity(self, obj):
        return obj.total_quantity

    def get_total_price(self, obj):
        return obj.total_price

    class Meta:
        model = CoffeeType
        exclude = ("deleted",)
        read_only_fields = (
            "external_id",
            "created_on",
            "modified_on",
            "owner",
        )


class CoffeeLogSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(source="external_id", read_only=True)

    class Meta:
        model = CoffeeLog
        exclude = ("deleted",)
        read_only_fields = (
            "external_id",
            "created_on",
            "modified_on",
            "coffee_type",
        )


class MentalHealthSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(source="external_id", read_only=True)

    class Meta:
        model = MentalHealth
        exclude = ("deleted",)
        read_only_fields = (
            "external_id",
            "created_on",
            "modified_on",
            "owner",
        )


class MentalHealthLogSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(source="external_id", read_only=True)

    class Meta:
        model = MentalHealthLog
        exclude = ("deleted",)
        read_only_fields = (
            "external_id",
            "created_on",
            "modified_on",
            "mental_health",
        )


class GoalSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(source="external_id", read_only=True)

    class Meta:
        model = Goal
        exclude = ("deleted",)
        read_only_fields = (
            "external_id",
            "created_on",
            "modified_on",
            "owner",
        )


class MilestoneSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(source="external_id", read_only=True)

    class Meta:
        model = Milestone
        exclude = (
            "deleted",
            "goal",
        )
        read_only_fields = (
            "external_id",
            "created_on",
            "modified_on",
            "completion_date",
        )


class MilestoneRoutineActivityRequirementSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(source="external_id", read_only=True)

    class Meta:
        model = MilestoneRoutineActivityRequirement
        exclude = (
            "deleted",
            "routine",
            "milestone",
        )
        read_only_fields = (
            "external_id",
            "created_on",
            "modified_on",
            "completed_by_activity",
        )


class MilestoneHabitRequirementSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(source="external_id", read_only=True)

    class Meta:
        model = MilestoneHabitRequirement
        exclude = (
            "deleted",
            "habit",
            "milestone",
        )
        read_only_fields = (
            "external_id",
            "created_on",
            "modified_on",
            "completed_by_habit",
        )
