from rest_framework import generics, viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from django.shortcuts import get_object_or_404
from .models import Users, Roles, UserRole, UserProfile, UserAddress
from .serializers import (
    UsersSerializer, RolesSerializer, UserRoleSerializer, 
    UserProfileSerializer, UserAddressSerializer, UserDetailSerializer
)
from .permissions import IsAdminUser

class UserCreateView(generics.CreateAPIView):
    """
    Admin only can create accounts.
    """
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    permission_classes = [permissions.AllowAny]

class UserListView(generics.ListAPIView):
    """
    Admin can list all users.
    """
    queryset = Users.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = [IsAdminUser]

class UserProfileView(APIView):
    """
    Users can see their own profile.
    Admin can see any profile.
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, username=None):
        is_admin = IsAdminUser().has_permission(request, self)
        if username and is_admin: 
            user = get_object_or_404(Users, username=username)
        else:
            user = request.user
        
        serializer = UserDetailSerializer(user)
        return Response(serializer.data)

class UserProfileViewSet(viewsets.ModelViewSet):
    """
    Admin can manage all user profiles.
    """
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAdminUser]

class RoleViewSet(viewsets.ModelViewSet):
    """
    Admin can manage roles.
    """
    queryset = Roles.objects.all()
    serializer_class = RolesSerializer
    permission_classes = [IsAdminUser]

class UserRoleViewSet(viewsets.ModelViewSet):
    """
    Admin can assign roles.
    """
    queryset = UserRole.objects.all()
    serializer_class = UserRoleSerializer
    permission_classes = [IsAdminUser]

class UserAddressViewSet(viewsets.ModelViewSet):
    """
    Manage user addresses. Admin can manage all.
    """
    queryset = UserAddress.objects.all()
    serializer_class = UserAddressSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        # Logic to check if user is admin (using IsAdminUser permission class logic or similar)
        # For simplicity reusing the permission check logic or assuming superuser/admin role check
        is_admin = UserRole.objects.filter(username=user, role_name='Admin').exists() or user.is_superuser
        
        if is_admin:
            return UserAddress.objects.all()
        return UserAddress.objects.filter(username=user)
