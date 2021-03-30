# Create your views here.

from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings


def index(request):
    context = {
        "data": "frist temp",
        "list": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    }
    return render(request, "index.html", context)


def contact(request):
    msg = {}
    if request.method == "POST":
        fname = request.POST['fname']
        email = request.POST['email']

        formail = f'Name : {fname}\n\nEmail : {email}'
        send_mail(
            'Mail From Site',
            formail,
            settings.EMAIL_HOST_USER,
            ['info@spangle.in'],
            fail_silently=False,
        )
        msg = {
            'msg': '***** Message Sent *****'
        }

    return render(request, "contact.html", msg)


def puranpatra(request):
    return render(request, "puranpatra.html")


def sinhasan(request):
    return render(request, "sinhasan.html")
