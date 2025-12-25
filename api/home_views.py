from django.shortcuts import render
from alerts.models import Alert
from users.decoraters import admin_required


@admin_required
def alert_list_view(request):
    alerts = Alert.objects.select_related("event").order_by("-created_at")

    context = {
        "alerts": alerts,
    }
    print(alerts)

    return render(request, "alerts/list.html", context)
