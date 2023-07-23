from rest_framework import routers

from .views import (
    CoffeeLogViewSet,
    CoffeeTypeViewSet,
    GoalViewSet,
    MentalHealthLogViewSet,
    MentalHealthViewSet,
    MilestoneRoutineActivityRequirementViewSet,
    MilestoneViewSet,
    RoutineActivityLogViewSet,
    RoutineActivityViewSet,
)

ilgi_router = routers.SimpleRouter()
ilgi_router.register(r"ilgi/coffee-log", CoffeeLogViewSet)
ilgi_router.register(r"ilgi/coffee-type", CoffeeTypeViewSet)
ilgi_router.register(r"ilgi/goal", GoalViewSet)
ilgi_router.register(r"ilgi/mental-health", MentalHealthViewSet)
ilgi_router.register(r"ilgi/mental-health-log", MentalHealthLogViewSet)
ilgi_router.register(r"ilgi/milestone", MilestoneViewSet)
ilgi_router.register(
    r"ilgi/milestone-routine-activity-requirement",
    MilestoneRoutineActivityRequirementViewSet,
)
ilgi_router.register(r"ilgi/routine-activity", RoutineActivityViewSet)
ilgi_router.register(r"ilgi/routine-activity-log", RoutineActivityLogViewSet)
