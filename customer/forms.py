from django import forms
from django.contrib.auth.models import User
from .models import Customer
from shopkeeper.models import Shopkeeper

class CustomerForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model=User
        fields=['first_name','last_name','username','email','password']

SHOP_CHOICES = (
    ('A','A'),
    ('B','B'),
    ('C','C')
)

# def lister(type):
ls=list()
for shops in Shopkeeper.objects.all():
    ls.append((shops.shop_name,shops.shop_name))
ls=tuple(ls)

# check this function
class customer_settings(forms.ModelForm):
    # shop_list=forms.CheckboxSelectMultiple(choices=ls)
    # shop_list=forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=ls)
    prefftime1 = forms.TimeField(widget=forms.TextInput(attrs={'type': 'time'}),label='Preferred Time 1')
    prefftime2 = forms.TimeField(widget=forms.TextInput(attrs={'type': 'time'}),label='Preferred Time 2' )
    prefftime3 = forms.TimeField(widget=forms.TextInput(attrs={'type': 'time'}),label='Preferred Time 3' )
    # shop_list = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=ls)
    class Meta():
        model=Customer
        fields=['prefftime1','prefftime2','prefftime3']    
        
class customer_name(forms.ModelForm):
    class Meta():
        model=User
        fields=['first_name','last_name','email']