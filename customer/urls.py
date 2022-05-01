from django.urls import path, include
from . import views

app_name = 'customer'
urlpatterns = [
    path('', views.index, name='customer'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.userLogout, name='logout'),
    path('query/', views.query, name='query'),
    path('shops/',views.interested_shops,name='shops')
    # path('profile/',views.profile,name="profile"),
]
