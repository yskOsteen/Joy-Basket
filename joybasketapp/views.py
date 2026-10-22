from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST

from .models import Contact


def home(request):
    return render(request, 'index.html')


def starter(request):
    return render(request, 'starter-page.html')


def service_details(request):
    return render(request, 'jservice-details.html')


def portfolio_details(request):
    return render(request, 'portfolio-details.html')

def show(request):
    all = Contact.objects.all()
    return render(request, 'show.html', {'all': all})


@require_POST
def contact(request):
    mycontact = Contact(
        name=request.POST.get('name', ''),
        email=request.POST.get('email', ''),
        phone=request.POST.get('phone', ''),
        subject=request.POST.get('subject', ''),
        message=request.POST.get('message', ''),
    )
    mycontact.save()
    return HttpResponse('OK')  # the template's JavaScript expects exactly "OK"


@require_POST
def newsletter(request):
    email = request.POST.get('email', '')
    send_mail('New newsletter signup', f'Subscribe: {email}', None, ['contact@example.com'])
    return HttpResponse('OK')