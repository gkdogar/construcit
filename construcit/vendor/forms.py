from django import forms
from django.forms import ModelForm


from .models.models import *


class VendorForm(ModelForm):

    class Meta:
        model =Vendor
        fields='__all__'