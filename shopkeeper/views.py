from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import shop_settings, shopkeeper_name, shopkeeperForm
from .models import Shopkeeper
from customer.models import Customer


########### Home/Index Page #########################################

@login_required(login_url='login/')
def index(request):
    if not user_check(request):
        return render(request,'shopkeeper/401.html',status=401)
    customer_list=Customer.objects.all() 
    ls=[]
    print(request.user.shopkeeper.id)
    for customer in customer_list:
        temp = str(customer.bit)
        try:
            temp[int(request.user.shopkeeper.id)-1]=='1'
            ls.append(customer)
        except IndexError:
            continue   
    return render(request, 'shopkeeper/index.html',{'Customer_list':ls})

############ Profile Page ##################################

@login_required(login_url='login/')
def profile(request):
    if not user_check(request):
        return render(request,'shopkeeper/401.html',status=401)
    return render(request, 'shopkeeper/profile.html')

########### Settings Page #####################################

@login_required(login_url='login/')
def settings(request):
    if not user_check(request):
        return render(request,'shopkeeper/401.html',status=401)  
    profile=request.user.shopkeeper
    if request.method == 'POST':
        form = shop_settings(request.POST,instance=profile)
        form_name=shopkeeper_name(request.POST,instance=request.user)
        if form.is_valid and form_name.is_valid is not None:
            form.save() and form_name.save()
    else:
        form=shop_settings(instance=profile)
        form_name=shopkeeper_name(instance=request.user)
    return render(request, 'shopkeeper/settings.html',{'form':form,'form_name':form_name})


########### Register Page #####################################

def register(request):
    if request.method == 'POST':
        form = shopkeeperForm(request.POST) 
        if form.is_valid() :
            add_user=form.save(commit=False)
            add_user.set_password(add_user.password)
            add_user.save()
            Shopkeeper.objects.create(user=add_user)

            # print(Shopkeeper.objects.filter(user=add_user).values())
            # username = form.cleaned_data.get('username')

            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('shopkeeper:login')
    else:
        form = shopkeeperForm()
    return render(request, 'shopkeeper/register.html', {'form': form})

################ Login Page ###################################

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        temp_user = authenticate(request, username=username, password=password)
        
        if temp_user is not None and hasattr(temp_user,'shopkeeper'):
            form = auth_login(request,temp_user)
            messages.success(request, f' welcome {username} !!')
            return redirect('shopkeeper:shopkeeper')
        else:
            messages.info(request, f'Account Does Not Exist Please Register')
    form = AuthenticationForm()
    return render(request, 'shopkeeper/login.html', {'form':form})

################ Logout ##############################

@login_required
def userLogout(request):
    logout(request)
    return redirect('home:index')

################ Shopkeeper Check ####################    

def user_check(request):
    if hasattr(request.user,'shopkeeper') :
        return True
    return False