from django.urls import include, path
from rest_framework.routers import DefaultRouter, SimpleRouter
from .settings import DEBUG


if DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

