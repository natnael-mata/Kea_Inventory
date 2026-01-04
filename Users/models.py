from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone

class UserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('status', 'Active')

        return self.create_user(username, password, **extra_fields)

class Users(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=150, primary_key=True)
    # Django requires 'password' attribute for AbstractBaseUser, 
    # but we can map it to 'password_hash' column
    password = models.CharField(max_length=128, db_column='password_hash')
    first_name = models.CharField(max_length=150, blank=True)
    middle_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    status = models.CharField(max_length=20, default='Active')
    created_on = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(null=True, blank=True, db_column='Last_login')
    created_by = models.CharField(max_length=150, null=True, blank=True)
    last_updated_on = models.DateTimeField(auto_now=True)
    last_updated_by = models.CharField(max_length=150, null=True, blank=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username
    
    class Meta:
        db_table = 'Users'

class Roles(models.Model):
    role_id = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=100)
    permission_type = models.CharField(max_length=100)
    effective_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.role_name

    class Meta:
        db_table = 'Roles'

class UserRole(models.Model):
    role_id = models.AutoField(primary_key=True) # Named role_id as requested, but it's the PK of this table
    username = models.ForeignKey(Users, on_delete=models.CASCADE, db_column='username')
    role_name = models.CharField(max_length=100)
    permission_type = models.CharField(max_length=100)
    effective_date = models.DateField(default=timezone.now)

    class Meta:
        db_table = 'UserRole'

class UserProfile(models.Model):
    profile_id = models.AutoField(primary_key=True)
    username = models.ForeignKey(Users, on_delete=models.CASCADE, db_column='username')
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'UserProfile'

class UserAddress(models.Model):
    address_id = models.AutoField(primary_key=True)
    username = models.ForeignKey(Users, on_delete=models.CASCADE, db_column='username')
    effective_date = models.DateField(default=timezone.now)
    country = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    woreda = models.CharField(max_length=100)
    kebele = models.CharField(max_length=100)
    house_no = models.CharField(max_length=50)
    phone_primary = models.CharField(max_length=20)
    Phone_secondary = models.CharField(max_length=20, blank=True, null=True) # Matching casing
    
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(Users, on_delete=models.SET_NULL, null=True, related_name='address_created_by', db_column='created_by')
    last_updated_on = models.DateTimeField(auto_now=True)
    last_updated_by = models.ForeignKey(Users, on_delete=models.SET_NULL, null=True, related_name='address_updated_by', db_column='last_updated_by')

    class Meta:
        db_table = 'UserAddress'
