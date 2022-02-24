from django.db import models
from django.contrib.auth.models import AbstractUser
from vendor.models.user_manager import *
from django.utils.translation import gettext_lazy as _
import jwt
from django.conf import settings
from datetime import datetime, timedelta

USER_CHOICES = (

    ('SUPER_ADMIN', 'Super Admin'),
    ('STAFF', 'Staff'),
    ('VENDOR', 'vendor'),

)




class User(AbstractUser):
    city = models.CharField(max_length=250, null=True)
    address = models.CharField(max_length=250, null=True)
    phone_no = models.CharField(max_length=250, null=True)
    user_type = models.CharField(max_length=16,
                                 choices=USER_CHOICES,
                                 default="CUSTOMER")

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    email = models.EmailField(_('email address'), unique=True)
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    @property
    def token(self):
        token = jwt.encode({'email': self.email, 'exp': datetime.utcnow() + timedelta(minutes=15)}, settings.SECRET_KEY,
                           algorithm='HS256')
        return token

    objects = UserManager()

    def __str__(self):
        return self.email
