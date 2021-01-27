from django.contrib import admin
from django.urls import path, include
from home.views import *
urlpatterns = [
    
    path('',index,name="index"),
    path('login',loginUser,name="login"),
    path('logout',logoutUser,name="logout")

    
]
