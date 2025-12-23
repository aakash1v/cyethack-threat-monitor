from django.db import models


class EventSeverity(models.TextChoices):
    LOW = "LOW", "Low"
    MEDIUM = "MEDIUM", "Medium"
    HIGH = "HIGH", "High"
    CRITICAL = "CRITICAL", "Critical"


class ThreatEvent(models.Model):
    source_name = models.CharField(max_length=255)
    event_type = models.CharField(max_length=100)
    severity = models.CharField(
        max_length=20, choices=EventSeverity.choices, db_index=True
    )
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["severity"]),
            models.Index(fields=["created_at"]),
        ]

    def __str__(self):
        return f"{self.event_type} | {self.severity}"
