from django.urls import include, path
from django.conf.urls import url,include
from rest_framework.authtoken import views





urlpatterns = [
    path('login/', include('rest_auth.urls')),
    path('registration/', include('rest_auth.registration.urls')),


   
]