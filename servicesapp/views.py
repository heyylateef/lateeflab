from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib import messages
from .forms import ContactForm
import os
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.utils.timezone import activate
from django.template.loader import render_to_string
#from cart.cart import Cart #django-cart, installed using github url with pip
#import stripe
import json
import pytz



def home(request):
    return render(request, 'servicesapp/home.html', {})

def privacypolicy(request):
    return render(request, 'privacypolicy.html', {})

def termsandconditions(request):
    return render(request, 'termsandconditions.html', {})

def pricing(request):
    return render(request, 'servicesapp/pricing.html', {})

def portfolio(request):
    return render(request, 'servicesapp/portfolio.html', {})

def about(request):
    return render(request, 'servicesapp/about.html', {})

def services_ecommerce(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            name = form.cleaned_data.get('name')
            message = form.cleaned_data.get('message')
            email_inquiry(name=name, email=email, message=message, serviceType="E-Commerce")
            messages.success(request, message="Email was sent successfully!")
            return render(request, 'servicesapp/services_ecommerce.html', {'form':form,})
        else:
            messages.error(request, "Error processesing emails, please try again")
            return render(request, 'servicesapp/services_ecommerce.html', {'form':form,})
    else:
        form = ContactForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'servicesapp/services_ecommerce.html', {'form':form,})

def services_blog(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            name = form.cleaned_data.get('name')
            message = form.cleaned_data.get('message')
            email_inquiry(name=name, email=email, message=message, serviceType="Blog")
            messages.success(request, message="Email was sent successfully!")
            return render(request, 'servicesapp/services_blog.html', {'form':form,})
        else:
            messages.error(request, "Error processesing emails, please try again")
            return render(request, 'servicesapp/services_blog.html', {'form':form,})
    else:
        form = ContactForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'servicesapp/services_blog.html', {'form':form,})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            name = form.cleaned_data.get('name')
            message = form.cleaned_data.get('message')
            email_inquiry(name=name, email=email, message=message, serviceType="Inquiry")
            messages.success(request, message="Email was sent successfully!")
            return render(request, 'servicesapp/contact.html', {'form':form,})
        else:
            messages.error(request, "Error processesing emails, please try again")
            return render(request, 'servicesapp/contact.html', {'form':form,})
    else:
        form = ContactForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'servicesapp/contact.html', {'form':form,})

# def contact_us_form(request):
#     contactName = request.GET.get('contactName', None) #Gets "contactFirstName" from AJAX function
#     contactEmail = request.GET.get('contactEmail', None) #Gets "contactEmail" from AJAX function
#     serviceType = request.GET.get('serviceType', None) #Gets "contactType" from AJAX function
#     contactMessage = request.GET.get('contactMessage', None) #Gets "contactMessage" from AJAX function
#     data ={
#         'contactName': contactName,    #contactFirstName from AJAX function as a dictionary
#         'contactEmail':contactEmail,
#         'serviceType':serviceType,
#         'contactMessage':contactMessage,
#     }
#     email_inquiry(name=contactName, email=contactEmail, message=contactMessage, serviceType=serviceType)

#     return JsonResponse(data)

def services_api(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            name = form.cleaned_data.get('name')
            message = form.cleaned_data.get('message')
            email_inquiry(name=name, email=email, message=message, serviceType="API")
            messages.success(request, message="Email was sent successfully!")
            return render(request, 'servicesapp/services_api.html', {'form':form,})
        else:
            messages.error(request, "Error processesing emails, please try again")
            return render(request, 'servicesapp/services_api.html', {'form':form,})
    else:
        form = ContactForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'servicesapp/services_api.html', {'form':form,})

def email_inquiry(name, email, message, serviceType, phone=None, date=None,):
    msg_plain = render_to_string('servicesapp/email_inquiry.txt', {'contactName':name, 'contactEmail':email, 'contactPhone':phone, 'contactDate':date, 'contactMessage':message,})
    msg_html = render_to_string('servicesapp/email_inquiry.html', {'contactName':name, 'contactEmail':email, 'contactPhone':phone, 'contactDate':date, 'contactMessage':message,})
    send_mail(subject=serviceType,message=msg_plain,from_email=settings.EMAIL_HOST_USER, recipient_list=[settings.EMAIL_HOST_USER], html_message=msg_html)

def beta(request):
    return render(request, 'servicesapp/contact.html', {})

# Create your views here.
