from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NetworkElementViewSet

router = DefaultRouter()
router.register(r"network_elements", NetworkElementViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
