from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import TownViewSet, StopViewSet, TransportViewSet

router = DefaultRouter()
router.register(r'town', TownViewSet, basename='town')
router.register(r'stop', StopViewSet, basename='stop')
router.register(r'transport', TransportViewSet, basename='transport')


urlpatterns = [
    path('', include(router.urls)),
]