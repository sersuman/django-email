from django.shortcuts import render
from django.core.mail import send_mail

def index(request):
    send_mail("Hellow from suman",'This is automated message','sumanshrestha670@gmail.com',['rigbuggy@gmail.com'],fail_silently=False)
    return render(request, 'send/index.html')
