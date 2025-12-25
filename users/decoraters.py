from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect


def admin_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        user = request.user

        if not user.is_authenticated:
            return redirect("login")

        if not hasattr(user, "profile"):
            raise PermissionDenied

        if user.profile.role not in ["ADMIN", "ANALYST"]:
            raise PermissionDenied

        return view_func(request, *args, **kwargs)

    return _wrapped_view
