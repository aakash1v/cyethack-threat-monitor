from django.contrib import admin
from django.urls import path

from threats.views import ThreatEventCreateAPIView
from alerts.views import AlertListAPIView, AlertStatusUpdateAPIView

urlpatterns = [

    path("events/", ThreatEventCreateAPIView.as_view()),
    path("alerts/", AlertListAPIView.as_view()),
    path("alerts/<int:pk>/status/", AlertStatusUpdateAPIView.as_view()),
]

