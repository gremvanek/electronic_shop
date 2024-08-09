from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomUserViewSet, LogoutView
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r"users", CustomUserViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("auth/token/login/", obtain_auth_token, name="token_login"),
    path("auth/token/logout/", LogoutView.as_view(), name="token_logout"),
]
