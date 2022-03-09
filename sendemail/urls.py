from rest_framework import routers
from . import views
from .views import api
from django.urls import path

urlpatterns = [
    path('email/', api, name = 'email')
]