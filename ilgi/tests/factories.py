from datetime import timezone

import factory
from django.contrib.auth import get_user_model
from factory.django import DjangoModelFactory

from ..models import (
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

User = get_user_model()


class RoutineActivityFactory(DjangoModelFactory):
    class Meta:
        model = RoutineActivity

    start_time = factory.Faker("date_time", tzinfo=timezone.utc)
    end_time = factory.Faker("date_time", tzinfo=timezone.utc)
    days_of_the_week = factory.Faker("random_int")
    label = factory.Faker("bs")
    owner = factory.SubFactory("users.tests.factories.UserFactory")


class RoutineActivityLogFactory(DjangoModelFactory):
    class Meta:
        model = RoutineActivityLog

    routine = factory.SubFactory("ilgi.tests.factories.RoutineActivityFactory")
    start_time = factory.Faker("date_time", tzinfo=timezone.utc)
    end_time = factory.Faker("date_time", tzinfo=timezone.utc)
    remarks = factory.Faker("text")
    timestamp = factory.Faker("date_time", tzinfo=timezone.utc)


class CoffeeLogFactory(DjangoModelFactory):
    class Meta:
        model = CoffeeLog

    quantity = factory.Faker(
        "pydecimal", left_digits=1, right_digits=3, min_value=None, max_value=None
    )
    type = factory.SubFactory("ilgi.tests.factories.CoffeeTypeFactory")


class CoffeeTypeFactory(DjangoModelFactory):
    class Meta:
        model = CoffeeType

    label = factory.Faker("bs")
    price = factory.Faker("random_int")


class MentalHealthFactory(DjangoModelFactory):
    class Meta:
        model = MentalHealth

    label = factory.Faker("bs")


class MentalHealthLogFactory(DjangoModelFactory):
    class Meta:
        model = MentalHealthLog

    mental_health = factory.SubFactory("ilgi.tests.factories.MentalHealthFactory")
    score = factory.Faker("random_int")


class GoalFactory(DjangoModelFactory):
    class Meta:
        model = Goal

    label = factory.Faker("bs")


class MilestoneFactory(DjangoModelFactory):
    class Meta:
        model = Milestone

    label = factory.Faker("bs")


class MilestoneRoutineActivityRequirementFactory(DjangoModelFactory):
    class Meta:
        model = MilestoneRoutineActivityRequirement

    routine = factory.SubFactory("ilgi.tests.factories.RoutineActivityFactory")
    count = factory.Faker("random_int")
    completed_by_activity = factory.SubFactory(
        "ilgi.tests.factories.RoutineActivityLogFactory"
    )
