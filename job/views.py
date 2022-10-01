from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from .filters import JobFilter
from .models import job
from django.core.paginator import Paginator
from .forms import applyform , jobForm
# Create your views here.

def job_list(request):
    job_list = job.objects.all()

    # filters
    myfilter = JobFilter(request.GET, queryset=job_list)
    job_list = myfilter.qs

    paginator = Paginator(job_list , 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'jobs':page_obj, 'myfilter':myfilter}
    return render(request,'job/job_list.html', context)

def job_detail(request, slug):
    job_detail = job.objects.get(slug=slug)
    if request.method =='POST':
        form = applyform(request.POST ,request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.job = job_detail
            myform.save()
    else:
        form = applyform()
    context = {'job': job_detail , 'form':form}
    return  render(request,'job/job_detail.html', context)

@login_required
def add_job(request):
    if request.method=='POST':
        form = jobForm(request.POST , request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.owner = request.user
            myform.save()
            return redirect(reverse('jobs:job_list'))
    else:
        form = jobForm
    return render(request,'job/add_job.html',{'form':form})