import uuid
from django.db import models
from django.urls import reverse_lazy
from django.contrib.auth.models import (
	AbstractBaseUser, BaseUserManager,
)


class UserManager(BaseUserManager):
    def create_user(self, name=None, surname=None, username=None, email=None, password=None, **kwargs):
        if email is None:
            raise TypeError('Users must have an email address.')
        
        if password is None:
            raise TypeError('Users must have an email address.')

        user = self.model(email=self.normalize_email(email))
        user.name = name
        user.surname = surname
        user.username = username
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, username, password, **kwargs):
        user = self.create_user(username=username, email=email, password=password)
        user.is_superuser = True
        user.is_staff = True
        user.private_access = True
        user.save()
        return user

class User(AbstractBaseUser):
    id = models.UUIDField(
        primary_key=True,
        db_index=True,
        default=uuid.uuid4,
        editable=False
    )
    
    email = models.EmailField(max_length=256, unique=True)
    username = models.CharField(max_length=256, unique=True)

    name = models.CharField(max_length=64, blank=True, null=True)
    surname = models.CharField(max_length=64, blank=True, null=True)
    
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False) 
    is_staff = models.BooleanField(default=False)

    # Auth settings
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'username'
    ]

    objects = UserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

    def get_absolute_url(self,):
        return reverse_lazy('moder_user_detail', kwargs={'id': self.id})