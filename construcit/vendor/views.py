
from django.shortcuts import render, redirect
from .models.models import *
# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.


def homePage(request):
    return render(request, 'vendor/dashboard.html')


def vendor_List(request):
    employee_list = User.objects.all()
    context = {
        'employee_list': employee_list
    }
    return render(request, 'vendor/list.html', context)


# @login_required(login_url='shopkeeper:admin_login')
def vendor_Setup(request):
    if request.POST:

        employee_id = request.POST.get('employee_id') or None
        if employee_id:
            # employee_obj = Employee.objects.get(id=employee_id)
            # user = User.objects.get(id=employee_obj.user.id)
            # user.first_name = request.POST.get('first_name')
            # user.last_name = request.POST.get('last_name')
            # user.email = request.POST.get('email')
            # user.address = request.POST.get('address')
            # user.city = request.POST.get('city')
            # user.phone_no = request.POST.get('phone_no')
            # user.save()
            # employee_obj.user = user

            # employee_obj.description = request.POST.get('description')
            # employee_obj.target_assign = request.POST.get('target_assign')
            # employee_obj.target_achieved = request.POST.get('target_achieved')
            # employee_obj.area_designated = request.POST.get('area_designated')
            # employee_obj.is_active = request.POST.get('is_active') or False
            # employee_obj.save()
            messages.add_message(request, messages.SUCCESS, 'Record Updated Successfully')
            return redirect('shopkeeper:employee_list')

        else:
            print('hello')
           
          
    else:
            
        return render(request, 'vendor/setup.html')

