from django.contrib import admin
from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)


from threats.views import ThreatEventCreateAPIView
from alerts.views import AlertListAPIView, AlertStatusUpdateAPIView

urlpatterns = [
    path("auth/login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("auth/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path("events/", ThreatEventCreateAPIView.as_view()),
    path("alerts/", AlertListAPIView.as_view()),
    path("alerts/<int:pk>/status/", AlertStatusUpdateAPIView.as_view()),
]
