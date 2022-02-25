
from re import I
from tkinter.messagebox import NO
from django.shortcuts import render, redirect
from .models.models import *
from .forms import *
# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.


def homePage(request):
    return render(request, 'vendor/base/home.html')

def admin_dashboard(request):
    return render(request, 'vendor/dashboard.html') 

def vendor_List(request):
    vendor_list = Vendor.objects.all()
    context = {
        'vendor_list': vendor_list
    }
    return render(request, 'vendor/list.html', context)


# @login_required(login_url='shopkeeper:admin_login')
def vendor_Setup(request):
    if request.POST:
        print('req', request.FILES)
        endor_id =request.POST.get('endor_id', None)
        if endor_id:
            vendor_obj =Vendor.objects.get(id=endor_id)

            vendor_obj.first_name=request.POST.get('first_name', vendor_obj.first_name)
            vendor_obj.last_name=request.POST.get('last_name', vendor_obj.last_name)
            vendor_obj.email=request.POST.get('email', vendor_obj.email)
            vendor_obj.phone_no=request.POST.get('phone_no', vendor_obj.phone_no)
            vendor_obj.city=request.POST.get('city', vendor_obj.city)
            vendor_obj.address=request.POST.get('address', vendor_obj.address)
            vendor_obj.business_name=request.POST.get('business_name', vendor_obj.business_name)
            vendor_obj.business_logo=request.FILES.get('business_logo', vendor_obj.business_logo )
            vendor_obj.rating=request.POST.get('rating', vendor_obj.rating)
            vendor_obj.is_active=request.POST.get('is_active') or False

            vendor_obj.save()
            messages.add_message(request, messages.SUCCESS, 'Vendor Record Updated Successfully !')
            return redirect('vendor:vendor_list')

        else:
            form =VendorForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.add_message(request, messages.SUCCESS, 'Vendor Record Added Successfully !')
                return redirect('vendor:vendor_list')
            else:
                print('form Error', form.errors)
                messages.add_message(request, messages.ERROR, form.errors)
                return redirect('vendor:vendor_setup')
    else:
            
        return render(request, 'vendor/setup.html')

def vendor_Update(request, pk):
    try:
        vendor = Vendor.objects.get(id=pk)
        conext={
            'vendor':vendor
            
        }
        return render(request, 'vendor/setup.html',conext)   

    except:

        messages.add_message(request, messages.ERROR, 'Vendor Does Not Exist')
        return redirect('vendor:vendor_setup')


def vendor_Delete(request, pk):
    try:
        vendor = Vendor.objects.get(id=pk)
        vendor.delete()
        messages.add_message(request, messages.ERROR, 'Vendor Deleted Successfully !')
        return redirect('vendor:vendor_list')
    except:

        messages.add_message(request, messages.ERROR, 'Record Does not exist for this user')
        return redirect('vendor:vendor_list')
