from django.urls import path,include
from bgapi import views

urlpatterns = [  
    path('', views.get_users,name="get_func"),
]
