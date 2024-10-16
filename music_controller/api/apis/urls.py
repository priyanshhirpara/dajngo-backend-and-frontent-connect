from django.urls import path
from api.apis.views import RoomView

urlpatterns = [
    path('rooms/', RoomView.as_view(), name='rooms'),  # Add URL for RoomView
]