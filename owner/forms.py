from django import forms
from django.contrib.auth.models import User
from shopkeeper.models import Shopkeeper

class shop_settings(forms.ModelForm):
    opening_time = forms.TimeField(widget=forms.TextInput(attrs={'type': 'time'}) )
    closing_time = forms.TimeField(widget=forms.TextInput(attrs={'type': 'time'}) )
    class Meta():
        model=Shopkeeper
        fields=['opening_time','closing_time']    

