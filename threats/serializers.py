from rest_framework import serializers
from threats.models import ThreatEvent


class ThreatEventCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThreatEvent
        fields = [
            "id",
            "source_name",
            "event_type",
            "severity",
            "description",
            "created_at",
        ]
        read_only_fields = ("id", "created_at")

