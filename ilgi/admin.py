from django.contrib import admin

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


class CoffeeLogAdmin(admin.ModelAdmin):
    model = CoffeeLog


class CoffeeTypeAdmin(admin.ModelAdmin):
    model = CoffeeType


class GoalAdmin(admin.ModelAdmin):
    model = Goal


class MentalHealthAdmin(admin.ModelAdmin):
    model = MentalHealth


class MentalHealthLogAdmin(admin.ModelAdmin):
    model = MentalHealthLog


class MilestoneAdmin(admin.ModelAdmin):
    model = Milestone


class MilestoneRoutineActivityRequirementAdmin(admin.ModelAdmin):
    model = MilestoneRoutineActivityRequirement


class RoutineActivityAdmin(admin.ModelAdmin):
    model = RoutineActivity
    list_display = ["label", "discontinued_on"]
    search_fields = ["label"]


class RoutineActivityLogAdmin(admin.ModelAdmin):
    model = RoutineActivityLog
    list_display = ["routine"]
    list_select_related = True


admin.site.register(CoffeeLog, CoffeeLogAdmin)
admin.site.register(CoffeeType, CoffeeTypeAdmin)
admin.site.register(Goal, GoalAdmin)
admin.site.register(MentalHealth, MentalHealthAdmin)
admin.site.register(MentalHealthLog, MentalHealthLogAdmin)
admin.site.register(Milestone, MilestoneAdmin)
admin.site.register(
    MilestoneRoutineActivityRequirement, MilestoneRoutineActivityRequirementAdmin
)
admin.site.register(RoutineActivity, RoutineActivityAdmin)
admin.site.register(RoutineActivityLog, RoutineActivityLogAdmin)
