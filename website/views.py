from django.shortcuts import render
from .models import Service
from django.core.mail import send_mail

# Create your views here.
def home(request):
    service = Service.objects.all()
    return render(request, 'home.html', {'service': service})



def contact(request):
    if request.method == "POST":
    
        # DO THIS
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']


        # SEND EMAIL
        send_mail(
            message_name,
            message,
            message_email,
            ['sidekicks.dvsn@gmail.com'], # TO THIS EMAIL ADDRESS
            fail_silently=False,
        )
        return render(request,'contact.html',{'message_name':message_name})
    else: 
        return render(request, 'contact.html', {})