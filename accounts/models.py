from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self,email,name,username,active=True,password=None):
        if not username:
            raise ValueError('Users must have a username')
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email= self.normalize_email(email),
            name=name,
            username=username,
            is_active=active
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,name,username,active=True,password=None):
        user=self.create_user(
            email=self.normalize_email(email),
            password=password,
            name=name,
            username=username
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
class User(AbstractBaseUser):
    username = models.CharField(max_length=150,unique=True)
    email = models.EmailField(max_length=255,unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','name']

    def __str__(self):
        return self.username

    def has_perm(self,perm,obj=None):
        return True
    def has_module_perms(self,app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin