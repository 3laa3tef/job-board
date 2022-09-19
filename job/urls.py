from django.urls import path , include
from django.contrib import admin
from  . import views

urlpatterns = [
    path('', views.job_list),
    path('<int:id>', views.job_detail)

]