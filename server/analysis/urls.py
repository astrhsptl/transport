from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import GivedTransportViewSet, AlertViewSet, GivedTransportInfoViewSet

router = DefaultRouter()
router.register(r'gived_transport', GivedTransportViewSet, basename='gived_transport')
router.register(r'alert', AlertViewSet, basename='alert')
router.register(r'gived_transport_info', GivedTransportInfoViewSet, basename='gived_transport_info')



urlpatterns = [
    path('', include(router.urls)),
]