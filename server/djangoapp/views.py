# Uncomment the required imports before adding the code

# from django.shortcuts import render
# from django.http import HttpResponseRedirect, HttpResponse
# from django.contrib.auth.models import User
# from django.shortcuts import get_object_or_404, render, redirect
# from django.contrib.auth import logout
# from django.contrib import messages
# from datetime import datetime

from django.http import JsonResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
import logging
import json
from django.views.decorators.csrf import csrf_exempt
# from .populate import initiate


# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your views here.


# Login view
@csrf_exempt
def login_user(request):
    if request.method != "POST":
        return JsonResponse(
            {"error": "POST method required"},
            status=405
        )

    try:
        data = json.loads(request.body or b"{}")
    except (json.JSONDecodeError, UnicodeDecodeError):
        return JsonResponse(
            {"error": "Invalid JSON"},
            status=400
        )

    username = data.get("userName", "").strip()
    password = data.get("password", "")

    user = authenticate(
        request,
        username=username,
        password=password
    )

    if user is not None:
        login(request, user)
        return JsonResponse({
            "userName": username,
            "status": "Authenticated"
        })

    return JsonResponse({
        "userName": username,
        "error": "Invalid credentials"
    })


# Logout view
def logout_request(request):
    if request.method != "GET":
        return JsonResponse(
            {"error": "GET method required"},
            status=405
        )

    logout(request)

    return JsonResponse({
        "userName": ""
    })


# Registration view
@csrf_exempt
def registration(request):
    if request.method != "POST":
        return JsonResponse(
            {"error": "POST method required"},
            status=405
        )

    try:
        data = json.loads(request.body or b"{}")
    except (json.JSONDecodeError, UnicodeDecodeError):
        return JsonResponse(
            {"error": "Invalid JSON"},
            status=400
        )

    username = data.get("userName", "").strip()
    password = data.get("password", "")
    first_name = data.get("firstName", "").strip()
    last_name = data.get("lastName", "").strip()
    email = data.get("email", "").strip()

    if not all([
        username,
        password,
        first_name,
        last_name,
        email
    ]):
        return JsonResponse(
            {"error": "All fields are required"},
            status=400
        )

    if User.objects.filter(username=username).exists():
        return JsonResponse({
            "userName": username,
            "error": "Already Registered"
        })

    user = User.objects.create_user(
        username=username,
        first_name=first_name,
        last_name=last_name,
        email=email,
        password=password
    )

    login(request, user)

    logger.info("Registered user: %s", username)

    return JsonResponse({
        "userName": username,
        "status": "Authenticated"
    })
