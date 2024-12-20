from django.urls import path, include
from rest_framework.routers import DefaultRouter

from myapp.api_viewset import AccountViewSet

# Create a router and register our ViewSets with it.
router = DefaultRouter()
router.register(r'',AccountViewSet,)
