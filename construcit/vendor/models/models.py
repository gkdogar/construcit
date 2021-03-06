from unicodedata import decimal
from django.db import models
from django.contrib.auth.models import AbstractUser
from vendor.models.user_manager import *
from django.utils.translation import gettext_lazy as _

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

   

    objects = UserManager()

    def __str__(self):
        return self.email



class Vendor(models.Model):
    first_name = models.CharField(max_length=250, null=True)
    last_name = models.CharField(max_length=250, null=True)
    email = models.EmailField(_('email address'), unique=True)
    phone_no = models.CharField(max_length=250, null=True)
    city = models.CharField(max_length=250, null=True)
    address = models.CharField(max_length=250, null=True)
    business_name = models.CharField(max_length=250, null=True)
    business_logo = models.ImageField(upload_to='vendImage/logo')
    rating = models.DecimalField(max_digits=7, default=0.00, decimal_places=2)
    videofile = models.FileField(upload_to='landing/videos', null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.business_name
