from django.urls import path
from .views import *
urlpatterns = [
    path("register_login",RegisterLoginView.as_view(),name="register_login")
]
