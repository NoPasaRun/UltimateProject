from django.urls import path
from app.api import RegisterEndpoint, LoginEndpoint


urlpatterns = [
    path('register/', RegisterEndpoint.as_view(), name='register'),
    path('login/', LoginEndpoint.as_view(), name='login'),
]
