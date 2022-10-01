from django.shortcuts import render
from .models import Info
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def send_message(request):
    myinfo = Info.objects.first()

    if request.method == 'POST':
        Subject = request.POST.get('subject')
        Email = "info@sysgot.com"
        Message = request.POST.get('message')
        sender = request.POST.get('email')

        print(Subject)
        print(Email)
        print(Message)



        send_mail(
            Subject,
            Message + " " +sender,
            settings.EMAIL_HOST_USER,
            [Email],
    )
    return render(request,'contact/contact.html', {'myinfo':myinfo})
