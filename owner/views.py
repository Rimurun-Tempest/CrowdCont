from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from customer.models import Customer
from shopkeeper.models import Shopkeeper
from django.utils.datastructures import MultiValueDictKeyError
from .forms import shop_settings
import subprocess
import smtplib

########### Home Page #########################################

@login_required(login_url='login/')
def index(request):
    Customer_list=Customer.objects.all()
    Shop_list=Shopkeeper.objects.all()
    shopkeepers=[]
    file=open('input.txt','w')
    file.write(str(len(Shop_list))+'\n')
    for i in Shop_list:    
        file.write(str(i.shop_name).replace(' ','.')+'\n')
        file.write(str(i.capacity)+'\n')
        file.write(str(i.opening_time).replace(':','')[0:2]+'\n')
        file.write(str(i.closing_time).replace(':','')[0:2]+'\n')
    file.write(str(len(Customer_list))+'\n')
    for i in Customer_list:
        file.write(str(i.prefftime1).replace(':','')[0:2]+'\n')
        file.write(str(i.prefftime2).replace(':','')[0:2]+'\n')
        file.write(str(i.prefftime3).replace(':','')[0:2]+'\n')
        interest_list=i.bit
        num=0
        for x in range(len(interest_list)):
            if interest_list[x]=='1':
                num+=1
        file.write(str(num)+'\n')
        for x in range(len(interest_list)):
            if interest_list[x]=='1':
                file.write(str(Shop_list[x].shop_name).replace(' ','.')+'\n')
        file.close()
    if request.method=='POST':        
        proc=subprocess.run('./algo.exe',shell=True)
        file=open('output.txt','r')
        data=file.read().split('\n')
        print(data)
        iterate=0
        for i in Customer_list:
            time=data[iterate]
            # mailer(request,i.user.email,i,time)
            Customer.objects.filter(id=i.id).update(approved=True,alloted_time=time)    
            iterate+=1
        # print(proc)
    return render(request,'owner/index.html',{'Customer_list':Customer_list})


########### Shops-Settings Page #########################################

@login_required(login_url='login/')
def shops(request):
    Shop_list=Shopkeeper.objects.all()
    if request.method=='POST':

        profile=Shopkeeper.objects.filter(id=request.POST['select_shop']).first()

        form=shop_settings(request.POST,instance=profile)

        if form.is_valid():
            form.save()  
    else:
        form=shop_settings()
    return render(request,'owner/shops.html',{'form':form,'Shop_list':Shop_list})


################ Login Page ###################################


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        temp_user = authenticate(request, username=username, password=password)

        if temp_user is not None and temp_user.is_superuser  :
            form = auth_login(request, temp_user)
            messages.success(request, f' welcome {username} !!')
            return redirect('owner:owner')
        else:
            messages.info(request, f'Account Does Not Exist Please Register')
    form = AuthenticationForm()
    return render(request, 'customer/login.html', {'form': form})


################ Logout ##############################

@login_required
def userLogout(request):
    logout(request)
    return redirect('home:index')


################ Email ################################

# def mailer(request,to_mail,name,alloted_time):
#     server =smtplib.SMTP('smtp.gmail.com',587)
#     server.starttls()
#     server.login(request.user.email,'')
#     text=f'Hello {name}, You have been alloted the time {alloted_time}. \n Kindly arrive at the Shopping Mall at your alloted time. \n Happy Shopping'
#     server.sendmail(request.user.email,to_mail,text)