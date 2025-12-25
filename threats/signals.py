from django.db.models.signals import post_save
from django.dispatch import receiver

from threats.models import ThreatEvent, EventSeverity
from alerts.models import Alert


@receiver(post_save, sender=ThreatEvent)
def create_alert_for_high_severity(sender, instance, created, **kwargs):
    if not created:
        return

    if instance.severity in {EventSeverity.HIGH, EventSeverity.CRITICAL}:
        Alert.objects.create(event=instance)

