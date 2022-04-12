from django.urls import path,include
from . import views

app_name='home'

urlpatterns = [
    path('',views.index,name='index'),
    path('logout',views.logout_view,name='logout'),
]
