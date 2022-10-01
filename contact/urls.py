from django.urls import path , include
from django.contrib import admin
from  . import views

app_name = 'contact'

urlpatterns = [
    path('', views.send_message ,name='contact'),

]