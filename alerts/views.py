import logging
from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated

from alerts.models import Alert
from alerts.serializers import AlertSerializer, AlertStatusUpdateSerializer
from users.permissions import IsAnalystReadOnly, IsAdmin

logger = logging.getLogger(__name__)


class AlertListAPIView(generics.ListAPIView):
    """
    List all alerts.
    - Admin: full access
    - Analyst: read-only access
    Supports filtering by status and severity.
    """

    queryset = Alert.objects.select_related("event")
    serializer_class = AlertSerializer
    permission_classes = [IsAuthenticated, IsAnalystReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ["status", "event__severity"]


class AlertStatusUpdateAPIView(generics.UpdateAPIView):
    queryset = Alert.objects.all()
    serializer_class = AlertStatusUpdateSerializer
    permission_classes = [IsAuthenticated, IsAdmin]

    def perform_update(self, serializer):
        alert = serializer.save()
        logger.info(
            "Alert %s status updated to %s by user %s",
            alert.id,
            alert.status,
            self.request.user.username,
        )
