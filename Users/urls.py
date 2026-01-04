from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import (
    UserCreateView, UserListView, UserProfileView, 
    RoleViewSet, UserRoleViewSet, UserAddressViewSet, UserProfileViewSet
)

router = DefaultRouter()
router.register(r'roles', RoleViewSet)
router.register(r'user-roles', UserRoleViewSet)
router.register(r'addresses', UserAddressViewSet)
router.register(r'user-profiles', UserProfileViewSet)

urlpatterns = [
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', UserCreateView.as_view(), name='user-register'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    path('profile/<str:username>/', UserProfileView.as_view(), name='user-profile-detail'),
    path('', include(router.urls)),
]
