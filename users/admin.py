from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

from .models import UserProfile

User = get_user_model()

# Unregister default User admin
admin.site.unregister(User)


class UserProfileInline(admin.StackedInline):
    """
    Inline UserProfile for role management.
    Auto-created via signals.
    """
    model = UserProfile
    can_delete = False
    extra = 0
    verbose_name_plural = "Profile"


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    """
    Custom User admin:
    - Removes groups & permissions
    - Adds role via UserProfile inline
    - Keeps auth system intact
    """

    inlines = (UserProfileInline,)

    # Clean list view
    list_display = (
        "username",
        "first_name",
        "last_name",
        "get_role",
        "is_active",
        "is_staff",
    )

    list_filter = ("is_active", "is_staff")
    search_fields = ("username", "first_name", "last_name")
    ordering = ("username",)

    # REMOVE groups & permissions from forms
    filter_horizontal = ()

    # Define clean fieldsets (edit user)
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Personal Info", {"fields": ("first_name", "last_name", "email")}),
        ("Status", {"fields": ("is_active", "is_staff", "is_superuser")}),
        ("Important Dates", {"fields": ("last_login", "date_joined")}),
    )

    # Define clean fieldsets (add user)
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "password1",
                    "password2",
                    "is_active",
                    "is_staff",
                ),
            },
        ),
    )

    readonly_fields = ("last_login", "date_joined")

    def get_role(self, obj):
        """
        Display role from UserProfile in list view.
        """
        if hasattr(obj, "profile"):
            return obj.profile.role
        return "-"
    get_role.short_description = "Role"
    get_role.admin_order_field = "profile__role"

