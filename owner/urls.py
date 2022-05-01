from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'owner'

urlpatterns = [
    path('', views.index, name='owner'),
    path('login/', views.login, name='login'),
    path('logout/', views.userLogout, name='logout'),
    path('shops/',views.shops,name='shops'),
    path('admin/', admin.site.urls),    
]
