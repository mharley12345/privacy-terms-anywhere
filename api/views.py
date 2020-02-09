from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from rest_framework.decorators import api_view
import json
from database.models import Person

@csrf_exempt
@api_view(['POST'])
def register(request):
    print(request)
    data = json.loads(request.body)
    username = data['email']
    password1 = data['password1']
    password2 = data['password2']
    first_name = data['First Name']
    last_name = data['Last Name']
    user = Person(email=username,first_name=first_name,last_name=last_name)
    if len(username) <= 3:
        response = JsonResponse(
            {"error": "Username must be at least 3 characters."}, safe=True, status=500)
    elif len(password1) <= 5:
        response = JsonResponse(
            {"error": "Password must be at least 5 characters."}, safe=True, status=500)
    elif password1 != password2:
        response = JsonResponse(
            {"error": "The two password fields didn't match."}, safe=True, status=500)
    else:
        try:
            user.validate_unique()
        except ValidationError:
            response = JsonResponse(
                {"error": "A user with that username already exists."}, safe=True, status=500)
        else:
            user.set_password(password1)
            user.save()
            response = JsonResponse(
                {"key": str(user.auth_token)}, safe=True, status=201)
    return response


@csrf_exempt
@api_view(['POST'])
def login(request):
    print(request)
    data = json.loads(request.body)
    username = data['username']
    password = data['password']
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        response = JsonResponse(
            {"error": "User does not exist."}, safe=True, status=500)
    else:
        if user.check_password(password):
            response = JsonResponse(
                {"key": str(user.auth_token)}, safe=True, status=200)
        else:
            response = JsonResponse(
                {"error": "Unable to log in with provided credentials."}, safe=True, status=500)
    return response
