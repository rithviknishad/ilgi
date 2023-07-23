from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.timezone import now

from utils.models import BaseModel


class RoutineActivity(BaseModel):
    label = models.CharField(max_length=255, null=False)
    description = models.TextField(null=True)

    start_time = models.TimeField(null=False, help_text="Time of day to start activity")
    end_time = models.TimeField(null=False, help_text="Time of day to end activity")

    on_monday = models.BooleanField(
        null=False,
        default=False,
        db_index=True,
        help_text="Whether this activity is done on Mondays",
    )
    on_tuesday = models.BooleanField(
        null=False,
        default=False,
        db_index=True,
        help_text="Whether this activity is done on Tuesdays",
    )
    on_wednesday = models.BooleanField(
        null=False,
        default=False,
        db_index=True,
        help_text="Whether this activity is done on Wednesdays",
    )
    on_thursday = models.BooleanField(
        null=False,
        default=False,
        db_index=True,
        help_text="Whether this activity is done on Thursdays",
    )
    on_friday = models.BooleanField(
        null=False,
        default=False,
        db_index=True,
        help_text="Whether this activity is done on Fridays",
    )
    on_saturday = models.BooleanField(
        null=False,
        default=False,
        db_index=True,
        help_text="Whether this activity is done on Saturdays",
    )
    on_sunday = models.BooleanField(
        null=False,
        default=False,
        db_index=True,
        help_text="Whether this activity is done on Sundays",
    )

    discontinued_on = models.DateTimeField(
        null=True,
        editable=False,
        help_text="If not null, this activity is discontinued.",
    )

    owner = models.ForeignKey(
        "users.User",
        related_name="routines",
        on_delete=models.CASCADE,
        null=False,
        db_index=True,
        help_text="The user who owns this routine.",
    )

    def __str__(self):
        return self.label


class RoutineActivityLog(BaseModel):
    routine = models.ForeignKey(
        RoutineActivity,
        related_name="logs",
        on_delete=models.CASCADE,
        null=False,
        db_index=True,
        help_text="The routine activity this log is for.",
    )
    start_time = models.TimeField(
        null=False, help_text="Time of day the activity started"
    )
    end_time = models.TimeField(null=False, help_text="Time of day the activity ended")
    remarks = models.TextField(null=False)

    @property
    def duration(self):
        return self.end_time - self.start_time

    def __str__(self):
        return f"{self.routine} ({self.start_time} - {self.end_time})"


class Habit(BaseModel):
    label = models.CharField(max_length=255, null=False)
    description = models.TextField(null=True)
    owner = models.ForeignKey(
        "users.User",
        related_name="habits",
        on_delete=models.CASCADE,
        null=False,
        db_index=True,
        editable=False,
        help_text="The user who owns this habit.",
    )
    discontinued_on = models.DateTimeField(
        null=True,
        db_index=True,
        editable=False,
        help_text="If not null, this habit is discontinued.",
    )

    def __str__(self):
        return self.label


class HabitLog(BaseModel):
    habit = models.ForeignKey(
        Habit,
        related_name="logs",
        on_delete=models.CASCADE,
        null=False,
        db_index=True,
        editable=False,
        help_text="The habit this log is for.",
    )
    day = models.DateField(null=False)
    remarks = models.TextField(null=False)

    def __str__(self):
        return f"{self.habit} ({self.timestamp})"


class CoffeeType(BaseModel):
    label = models.CharField(max_length=255, null=False)
    price = models.IntegerField(null=False, help_text="Price per litre")

    owner = models.ForeignKey(
        "users.User",
        related_name="coffee_types",
        on_delete=models.CASCADE,
        null=False,
        db_index=True,
        help_text="The user who owns this coffee type.",
    )

    @property
    def total_quantity(self):
        return CoffeeLog.objects.filter(coffee_type=self).aggregate(
            models.Sum("quantity")
        )["quantity__sum"]

    @property
    def total_price(self):
        return self.total_quantity * self.price

    def __str__(self):
        return self.label


class CoffeeLog(BaseModel):
    quantity = models.DecimalField(
        null=False,
        max_digits=4,
        decimal_places=3,
        validators=[MinValueValidator(0.001), MaxValueValidator(1)],
        help_text="Quantity of coffee consumed in litres",
    )
    coffee_type = models.ForeignKey(
        CoffeeType,
        related_name="logs",
        on_delete=models.CASCADE,
        null=False,
        db_index=True,
        editable=False,
        help_text="The coffee type this log is for.",
    )
    timestamp = models.DateTimeField(
        null=False, default=now, help_text="Time of day the coffee was consumed"
    )

    def __str__(self):
        return f"{self.coffee_type} - {self.quantity}L ({self.timestamp})"


class MentalHealth(BaseModel):
    label = models.CharField(max_length=255, null=False)

    score_label_extremely_low = models.CharField(
        max_length=255, null=True, help_text="Score of -3"
    )
    score_label_very_low = models.CharField(
        max_length=255, null=True, help_text="Score of -2"
    )
    score_label_low = models.CharField(
        max_length=255, null=True, help_text="Score of -1"
    )
    score_label_neutral = models.CharField(
        max_length=255, null=True, help_text="Score of 0"
    )
    score_label_high = models.CharField(
        max_length=255, null=True, help_text="Score of 1"
    )
    score_label_very_high = models.CharField(
        max_length=255, null=True, help_text="Score of 2"
    )
    score_label_extremely_high = models.CharField(
        max_length=255, null=True, help_text="Score of 3"
    )

    owner = models.ForeignKey(
        "users.User",
        related_name="mental_health_metrics",
        on_delete=models.CASCADE,
        null=False,
        db_index=True,
    )

    def get_score_label(self, score):
        if score == -3:
            return self.score_label_extremely_low
        elif score == -2:
            return self.score_label_very_low
        elif score == -1:
            return self.score_label_low
        elif score == 0:
            return self.score_label_neutral
        elif score == 1:
            return self.score_label_high
        elif score == 2:
            return self.score_label_very_high
        elif score == 3:
            return self.score_label_extremely_high

        raise ValueError("Invalid mental health score.")

    def __str__(self):
        return self.label


class MentalHealthLog(BaseModel):
    mental_health = models.ForeignKey(
        MentalHealth,
        related_name="logs",
        on_delete=models.CASCADE,
        null=False,
        db_index=True,
        editable=False,
        help_text="The mental health metric this log is for.",
    )
    score = models.SmallIntegerField(
        null=False,
        validators=[MinValueValidator(-3), MaxValueValidator(3)],
        help_text="Score of the mental health metric",
    )
    timestamp = models.DateTimeField(null=False, default=now, help_text="Time of log")

    @property
    def get_score_label(self):
        return self.mental_health.get_score_label(self.score)

    def __str__(self):
        return f"{self.mental_health}: {self.score} - {self.status} ({self.timestamp})"


class Goal(BaseModel):
    label = models.CharField(max_length=255, null=False)
    description = models.TextField(null=True)

    owner = models.ForeignKey(
        "users.User",
        related_name="goals",
        on_delete=models.CASCADE,
        null=False,
        db_index=True,
        editable=False,
        help_text="The user who owns this goal.",
    )

    def __str__(self):
        return self.label


class Milestone(BaseModel):
    goal = models.ForeignKey(
        Goal,
        related_name="milestones",
        on_delete=models.CASCADE,
        null=False,
        db_index=True,
        editable=False,
        help_text="The goal this milestone is for.",
    )

    label = models.CharField(max_length=255, null=False)
    description = models.TextField(null=True)

    deadline = models.DateTimeField(
        null=True,
        help_text="If not null, this milestone has a deadline.",
    )
    completion_date = models.DateTimeField(
        null=True,
        editable=False,
        db_index=True,
        help_text="If not null, this milestone is completed.",
    )

    def __str__(self):
        return self.label


class MilestoneRoutineActivityRequirement(BaseModel):
    routine = models.ForeignKey(
        RoutineActivity,
        related_name="milestone_requirements",
        on_delete=models.CASCADE,
        null=False,
        editable=False,
        help_text="The routine activity this requirement is for.",
    )
    milestone = models.ForeignKey(
        Milestone,
        related_name="routine_requirements",
        on_delete=models.CASCADE,
        null=False,
        editable=False,
        db_index=True,
        help_text="The milestone this requirement is part of.",
    )

    count = models.IntegerField(null=False)
    description = models.TextField(null=True)

    completed_by_activity = models.ForeignKey(
        RoutineActivityLog,
        related_name="+",
        on_delete=models.CASCADE,
        null=False,
        db_index=True,
        editable=False,
        help_text="The routine activity log that completed this requirement.",
    )

    def __str__(self):
        return f"{self.milestone}: {self.routine} ({self.count})"


class MilestoneHabitRequirement(BaseModel):
    habit = models.ForeignKey(
        Habit,
        related_name="milestone_requirements",
        on_delete=models.CASCADE,
        null=False,
        editable=False,
        help_text="The habit this requirement is for.",
    )
    milestone = models.ForeignKey(
        Milestone,
        related_name="habit_requirements",
        on_delete=models.CASCADE,
        null=False,
        editable=False,
        db_index=True,
        help_text="The milestone this requirement is part of.",
    )

    count = models.IntegerField(null=False)
    description = models.TextField(null=True)

    completed_by_activity = models.ForeignKey(
        HabitLog,
        related_name="+",
        on_delete=models.CASCADE,
        null=False,
        db_index=True,
        editable=False,
        help_text="The habit log that completed this requirement.",
    )

    def __str__(self):
        return f"{self.milestone}: {self.habit} ({self.count})"
