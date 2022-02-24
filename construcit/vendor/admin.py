from django.contrib import admin
from .models.models import *
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from import_export.admin import ImportExportModelAdmin, post_export, post_import
# Register your models here.


@admin.register(User)
class UserAdmin(ImportExportModelAdmin, DjangoUserAdmin):
    """Define admin model for custom User model with no email field."""
    fieldsets = ((None, {
        'fields':
        ('first_name', 'last_name', 'email','city', 'phone_no','password', 'groups',
        'address','user_type')
    }), )
    add_fieldsets = ((None, {
        'classes': ('wide', ),
        'fields': ('email', 'password1', 'password2'),
    }), )
    list_display = ('email', 'first_name', 'last_name', 'user_type')
    search_fields = ('email', 'first_name', 'last_name', 'user_type')
    ordering = ('email', )
