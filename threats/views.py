from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from threats.models import ThreatEvent
from threats.serializers import ThreatEventCreateSerializer
from users.permissions import IsAdmin


class ThreatEventCreateAPIView(generics.CreateAPIView):
    queryset = ThreatEvent.objects.all()
    serializer_class = ThreatEventCreateSerializer
    permission_classes = [IsAuthenticated, IsAdmin]
