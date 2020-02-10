from django.contrib import admin
from django.shortcuts import render
from django.urls import include,re_path
from django.conf.urls import include,url
from rest_framework import routers
from api.urls import *
#from homepage.urls import *
#from homepage.views import answers,policy
from database.views import *
from rest_framework.authtoken import views
from forms_builder.forms.models import Form
from forms_builder.forms import urls as form_urls
router = routers.DefaultRouter()
router.register(r'sample', SamplePolicyViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    re_path(r'api-token-auth/', views.obtain_auth_token),
    re_path(r'^forms/', include(form_urls)),
    #path('homepage/policy/',include(policy)),
    #url('homepage/answers/',include(answers))
   
]
