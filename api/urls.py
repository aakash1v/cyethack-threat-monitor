from django.contrib import admin
from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from threats.views import ThreatEventCreateAPIView
from alerts.views import AlertListAPIView, AlertStatusUpdateAPIView

urlpatterns = [
    path("auth/login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("auth/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("events/", ThreatEventCreateAPIView.as_view()),
    path("alerts/", AlertListAPIView.as_view()),
    path("alerts/<int:pk>/status/", AlertStatusUpdateAPIView.as_view()),
]
