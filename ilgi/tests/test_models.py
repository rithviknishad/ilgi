from django.test import TestCase

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
from .factories import (
    CoffeeLogFactory,
    CoffeeTypeFactory,
    GoalFactory,
    MentalHealthFactory,
    MentalHealthLogFactory,
    MilestoneFactory,
    MilestoneRoutineActivityRequirementFactory,
    RoutineActivityFactory,
    RoutineActivityLogFactory,
)


class RoutineActivityTestCase(TestCase):
    def test_create_routine_activity(self):
        """Test that RoutineActivity can be created using its factory."""

        obj = RoutineActivityFactory()
        assert RoutineActivity.objects.all().get() == obj


class RoutineActivityLogTestCase(TestCase):
    def test_create_routine_activity_log(self):
        """Test that RoutineActivityLog can be created using its factory."""

        obj = RoutineActivityLogFactory()
        assert RoutineActivityLog.objects.all().get() == obj


class CoffeeLogTestCase(TestCase):
    def test_create_coffee_log(self):
        """Test that CoffeeLog can be created using its factory."""

        obj = CoffeeLogFactory()
        assert CoffeeLog.objects.all().get() == obj


class CoffeeTypeTestCase(TestCase):
    def test_create_coffee_type(self):
        """Test that CoffeeType can be created using its factory."""

        obj = CoffeeTypeFactory()
        assert CoffeeType.objects.all().get() == obj


class MentalHealthTestCase(TestCase):
    def test_create_mental_health(self):
        """Test that MentalHealth can be created using its factory."""

        obj = MentalHealthFactory()
        assert MentalHealth.objects.all().get() == obj


class MentalHealthLogTestCase(TestCase):
    def test_create_mental_health_log(self):
        """Test that MentalHealthLog can be created using its factory."""

        obj = MentalHealthLogFactory()
        assert MentalHealthLog.objects.all().get() == obj


class GoalTestCase(TestCase):
    def test_create_goal(self):
        """Test that Goal can be created using its factory."""

        obj = GoalFactory()
        assert Goal.objects.all().get() == obj


class MilestoneTestCase(TestCase):
    def test_create_milestone(self):
        """Test that Milestone can be created using its factory."""

        obj = MilestoneFactory()
        assert Milestone.objects.all().get() == obj


class MilestoneRoutineActivityRequirementTestCase(TestCase):
    def test_create_milestone_routine_activity_requirement(self):
        """Test that MilestoneRoutineActivityRequirement can be created using its factory."""

        obj = MilestoneRoutineActivityRequirementFactory()
        assert MilestoneRoutineActivityRequirement.objects.all().get() == obj
