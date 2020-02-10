# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework import serializers, viewsets
import json
import os

class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields =("id","username","first_name","last_name","password")

    def create(self,validate_data):
        user = self.context['request'].user
        people = Person.objects.create(**validate_data)
        return people

class PersonViewSet(viewsets.ModelViewSet):
    serializers_class = PersonSerializer

    def get_queryset(self):
        return Person.objects.all()
class SamplePolicySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SamplePolicys
        fields = ['id',"business_name","site_name","street_address","city","state","zipcode","email"]
class SamplePolicyViewSet(viewsets.ModelViewSet):
    serializer_class = SamplePolicySerializer
    queryset=SamplePolicys.objects.none()
    def get_queryset(self):
        return SamplePolicys.objects.all()



# Create your views here.

