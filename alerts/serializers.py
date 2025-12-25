from rest_framework import serializers
from alerts.models import Alert


class AlertSerializer(serializers.ModelSerializer):
    event = serializers.StringRelatedField()

    class Meta:
        model = Alert
        fields = [
            "id",
            "event",
            "status",
            "created_at",
        ]
        read_only_fields = ("id", "created_at")


class AlertStatusUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alert
        fields = ["status"]
