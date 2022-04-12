from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomerForm,customer_settings
from .models import Customer
from shopkeeper.models import Shopkeeper
from django.utils.datastructures import MultiValueDictKeyError
########### Home Page #########################################


@login_required(login_url='login/')
def index(request):
    Shop_list=Shopkeeper.objects.all()
    if not user_check(request):
        return render(request,'shopkeeper/401.html',status=401)
    ls=[]      
    temp=str(request.user.customer.bit)
    print(temp)
    # print(temp[0])
    for shop in Shop_list:
        if temp[int(shop.id)-1]=='1':
            ls.append(shop)
    print(ls)
    return render(request, 'customer/index.html',{'Shop_list':ls})

############ Profile Page ##################################


# @login_required(login_url='login/')
# def profile(request):

#     return render(request, 'customer/profile.html')

########### Query Page #####################################


@login_required(login_url='login/')
def query(request):
    Shop_list=Shopkeeper.objects.all()
    if not user_check(request):
        return render(request,'shopkeeper/401.html',status=401)      
    if request.method == 'POST':
        form=customer_settings(request.POST,instance=request.user.customer)
        s = ""
        for shop in Shop_list:
            temp=str(shop.id)
            try:
                request.POST[temp]
                s += '1'

            except MultiValueDictKeyError:
                s += '0'        
        print(s)
        if form.is_valid:
            form.save()
            Customer.objects.all().filter(user=request.user).update(bit=s)
    else:
        form=customer_settings(instance=request.user.customer)          
    return render(request, 'customer/query.html', {'form':form,'Shop_list':Shop_list})

########### Register Page #####################################

def register(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            add_user = form.save(commit=False)
            add_user.set_password(add_user.password)
            add_user.save()
            Customer.objects.create(user=add_user)

            # print(Shopkeeper.objects.filter(user=add_user).values())
            # username = form.cleaned_data.get('username')

            messages.success(
                request, 'Your account has been created! You are now able to log in')
            return redirect('customer:login')
    else:
        form = CustomerForm()
    return render(request, 'customer/register.html', {'form': form})

################ Login Page ###################################

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        temp_user = authenticate(request, username=username, password=password)

        if temp_user is not None and hasattr(temp_user,'customer'):
            form = auth_login(request, temp_user)
            messages.success(request, f' welcome {username} !!')
            return redirect('customer:customer')
        else:
            messages.info(request, f'Account Does Not Exist Please Register')
    form = AuthenticationForm()
    return render(request, 'customer/login.html', {'form': form})


################ Logout ##############################

@login_required
def userLogout(request):
    logout(request)
    return redirect('home:index')

################# User Check ########################

def user_check(request):
    if hasattr(request.user,'customer') :
        return True
    return False