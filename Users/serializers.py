from rest_framework import serializers
from .models import Users, Roles, UserRole, UserProfile, UserAddress

class UsersSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = Users
        fields = ['username', 'first_name', 'middle_name', 'last_name', 'status', 'password', 'created_on', 'last_login']
        read_only_fields = ['created_on', 'last_login']

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class RolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = '__all__'

class UserRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRole
        fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class UserAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAddress
        fields = '__all__'

class UserDetailSerializer(serializers.ModelSerializer):
    """
    Serializer for detailed user view including roles and address
    """
    roles = serializers.SerializerMethodField()
    address = serializers.SerializerMethodField()
    profile = UserProfileSerializer(source='userprofile', read_only=True)

    class Meta:
        model = Users
        fields = ['username', 'first_name', 'middle_name', 'last_name', 'status', 'last_login', 'roles', 'address', 'profile']

    def get_roles(self, obj):
        roles = UserRole.objects.filter(username=obj)
        return UserRoleSerializer(roles, many=True).data

    def get_address(self, obj):
        addresses = UserAddress.objects.filter(username=obj)
        return UserAddressSerializer(addresses, many=True).data
