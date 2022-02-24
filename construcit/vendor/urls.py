from django.urls import path, include
from django.conf.urls.static import static
from .views import *

app_name = 'vendor' 
urlpatterns = [

    path('', homePage, name='homePage'),
    path('vendor/lists', vendor_List, name='vendor_list'),
    path('vendor/setup', vendor_Setup, name='vendor_setup'),
     path('vendor/setup/<int:pk>/', vendor_Setup, name='vendor_update'),
    path('vendor/delete/<int:pk>/', vendor_Setup, name='vendor_delete'),
]