from django import forms
from django.contrib.auth.models import User
from .models import Shopkeeper

class shopkeeperForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model=User
        fields=['first_name','last_name','username','email','password']

SHOP_CHOICES = (
    ('A','A'),
    ('B','B'),
    ('C','C')
)
# class shopkeeperAddForm(forms.ModelForm):
#     type=forms.CharField(widget=forms.Select(choices=SHOP_CHOICES))
#     class Meta():
#         model=Shopkeeper
#         fields=['type']

class shop_settings(forms.ModelForm):
    type=forms.CharField(widget=forms.Select(choices=SHOP_CHOICES))
    opening_time = forms.TimeField(widget=forms.TextInput(attrs={'type': 'time'}) )
    closing_time = forms.TimeField(widget=forms.TextInput(attrs={'type': 'time'}) )
    class Meta():
        model=Shopkeeper
        fields=['shop_name','type','capacity','opening_time','closing_time','shop_bio']    
