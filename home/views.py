from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import redirect
# Create your views here.
def index(request):
    return render(request, 'home/index.html')

def logout_view(request):
    logout(request)
    return redirect('home:index')