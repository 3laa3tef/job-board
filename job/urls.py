from django.urls import path , include
from django.contrib import admin
from  . import views

app_name = 'job'

urlpatterns = [
    path('', views.job_list),
    path('<int:id>', views.job_detail , name='job_detail')

]