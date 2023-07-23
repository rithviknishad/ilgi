from django.contrib import admin
from django.contrib.auth import get_user_model

User = get_user_model()


class UserAdmin(admin.ModelAdmin):
    model = User
    list_display = ["email", "name", "is_active", "is_staff"]
    search_fields = ["email", "name"]
    list_filter = ["is_active", "is_staff"]


admin.site.register(User, UserAdmin)
