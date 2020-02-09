from django.contrib import admin
from django.urls import include,re_path
from django.conf.urls import include
from rest_framework import routers
from api.urls import *
from rest_framework.authtoken import views

router = routers.DefaultRouter()


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    re_path(r'api-token-auth/', views.obtain_auth_token)
]
