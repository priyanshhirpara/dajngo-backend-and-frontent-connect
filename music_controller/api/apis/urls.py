from django.urls import path
from api.apis.views import main

urlpatterns = [
    path('main/', main, name='main'),
]