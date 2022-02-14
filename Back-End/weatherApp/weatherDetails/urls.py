"""urls to route requests."""
from django.urls import path
#from .views import *
from . import views

urlpatterns = [
    path('get-forecast', views.getWeatherForcast.as_view(),name="get-forecast")
]