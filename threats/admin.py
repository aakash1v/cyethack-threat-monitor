from django.contrib import admin
from .models import ThreatEvent


@admin.register(ThreatEvent)
class ThreatEventAdmin(admin.ModelAdmin):
    list_display = ("event_type", "severity", "source_name", "created_at")
    list_filter = ("severity", "event_type")
    search_fields = ("source_name", "description")
