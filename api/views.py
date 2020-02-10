from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core.exceptions import ValidationError
from rest_framework.decorators import api_view
from database.models import Person,Policy
from rest_framework import serializers,fields
from database.views import SamplePolicySerializer
import json

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
    email = data['email']
    password = data['password']
    try:
        user = Person.objects.get(email=email)
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

@csrf_exempt
@api_view(["GET"])
def get_policy(request):
    fields = ['business_name','site_name','email','street_address','city','state','zipcode']
    serializer = SamplePolicySerializer
    response = serializer
    return response

@csrf_exempt
@api_view(['POST'])
def answers(request):
    print(request)
    data = json.loads(request.body)
    business_name= data['business_name']
    site_name = data['site_name']
    email = data['email']
    street_address = data['street_address']
    city = data['city']
    state = data['state']
    zipcode = data['zipcode']
    response = render('/homepage/answers.html')   
    return response