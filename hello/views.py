from django.shortcuts import redirect
from django.conf import settings
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)

def hello_world(request):
    if request.user.is_authenticated:
        message = f"Hello, {request.user.username}! You are authenticated."
    else:
        sso_login_url = f"http://localhost:8000/login/?next={request.build_absolute_uri()}"
        logger.debug(f"Redirecting to: {sso_login_url}")

        return redirect(sso_login_url)

    return HttpResponse(message)