from django.shortcuts import redirect
from django.conf import settings
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)

def hello_world(request):
    if request.user.is_authenticated:
        message = f"Hello, {request.user.username}! You are authenticated."
        return HttpResponse(message)
    else:
        # message = "You are not authenticated."
        redirect_url = "/login"
        return redirect(redirect_url)
