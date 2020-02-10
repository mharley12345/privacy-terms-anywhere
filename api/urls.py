from django.urls import include, path
from django.conf.urls import url,include
from rest_framework.authtoken import views
from .views import answers,get_policy




urlpatterns = [
    path('', include('rest_auth.urls')),
    path('registration/', include('rest_auth.registration.urls')),
    url('answers', answers),
    url('get_policy',get_policy)
   
]