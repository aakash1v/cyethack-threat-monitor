from django.conf import settings
from django.db import models

# print(settings.AUTH_USER_MODEL)


class UserRole(models.TextChoices):
    ADMIN = "ADMIN", "Admin"
    ANALYST = "ANALYST", "Analyst"


class UserProfile(models.Model):
    """
    Extends Django's built-in User with role information.
    Keeps auth system intact.
    """

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile"
    )
    role = models.CharField(
        max_length=20, choices=UserRole.choices, default=UserRole.ANALYST, db_index=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} ({self.role})"
