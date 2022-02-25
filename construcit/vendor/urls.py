from django.urls import path, include
from django.conf.urls.static import static
from .views import *

app_name = 'vendor' 
urlpatterns = [

    path('', homePage, name='homePage'),
    path('dashboard', admin_dashboard, name='admin_dashboard'),
    path('vendor/lists', vendor_List, name='vendor_list'),
    path('vendor/setup', vendor_Setup, name='vendor_setup'),
    path('vendor/setup/<int:pk>/', vendor_Update, name='vendor_update'),
    path('vendor/delete/<int:pk>/', vendor_Delete, name='vendor_delete'),
    path('login', admin_login, name='admin_login'),
    path('logout', admin_logout, name='admin_logout'),
    path('settings', admin_settings, name='admin_setting'),
]