from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib import messages
from .forms import ContactForm
from django.conf import settings
from django.core.mail import send_mail
from django.utils.timezone import activate
from django.template.loader import render_to_string
#from cart.cart import Cart #django-cart, installed using github url with pip
#import stripe



def home(request):
    return render(request, 'servicesapp/home.html', {})

def privacypolicy(request):
    return render(request, 'privacypolicy.html', {})

def termsandconditions(request):
    return render(request, 'termsandconditions.html', {})

def about(request):
    return render(request, 'servicesapp/about.html', {})

def templates(request):
    #selling templates
    return

def services_ecommerce(request):
    # if request.method == 'POST':
    #     form = ContactForm(request.POST)
    #     if form.is_valid():
    #         email = form.cleaned_data.get('email')
    #         name = form.cleaned_data.get('name')
    #         message = form.cleaned_data.get('message')
    #         email_inquiry(name=name, email=email, message=message, serviceType="E-Commerce")
    #         messages.success(request, message="Email was sent successfully!")
    #         return render(request, 'servicesapp/services_ecommerce.html', {'form':form,})
    #     else:
    #         messages.error(request, "Error processesing emails, please try again")
    #         return render(request, 'servicesapp/services_ecommerce.html', {'form':form,})
    # else:
    #     form = ContactForm()
    #     if 'submitted' in request.GET:
    #         submitted = True
    return render(request, 'servicesapp/services_ecommerce.html', {})

def services_blog(request):
    # if request.method == 'POST':
    #     form = ContactForm(request.POST)
    #     if form.is_valid():
    #         email = form.cleaned_data.get('email')
    #         name = form.cleaned_data.get('name')
    #         message = form.cleaned_data.get('message')
    #         email_inquiry(name=name, email=email, message=message, serviceType="Blog")
    #         messages.success(request, message="Email was sent successfully!")
    #         return render(request, 'servicesapp/services_blog.html', {'form':form,})
    #     else:
    #         messages.error(request, "Error processesing emails, please try again")
    #         return render(request, 'servicesapp/services_blog.html', {'form':form,})
    # else:
    #     form = ContactForm()
    #     if 'submitted' in request.GET:
    #         submitted = True
    return render(request, 'servicesapp/services_blog.html', {})

def contact(request):
    # if request.method == 'POST':
    #     form = ContactForm(request.POST)
    #     if form.is_valid():
    #         email = form.cleaned_data.get('email')
    #         name = form.cleaned_data.get('name')
    #         message = form.cleaned_data.get('message')
    #         email_inquiry(name=name, email=email, message=message, serviceType="Inquiry")
    #         messages.success(request, message="Email was sent successfully!")
    #         return render(request, 'servicesapp/contact.html', {'form':form,})
    #     else:
    #         messages.error(request, "Error processesing emails, please try again")
    #         return render(request, 'servicesapp/contact.html', {'form':form,})
    # else:
    #     form = ContactForm()
    #     if 'submitted' in request.GET:
    #         submitted = True
    return render(request, 'servicesapp/contact.html', {})

def services_api(request):
    # if request.method == 'POST':
    #     form = ContactForm(request.POST)
    #     if form.is_valid():
    #         email = form.cleaned_data.get('email')
    #         name = form.cleaned_data.get('name')
    #         message = form.cleaned_data.get('message')
    #         email_inquiry(name=name, email=email, message=message, serviceType="API")
    #         messages.success(request, message="Email was sent successfully!")
    #         return render(request, 'servicesapp/services_api.html', {'form':form,})
    #     else:
    #         messages.error(request, "Error processesing emails, please try again")
    #         return render(request, 'servicesapp/services_api.html', {'form':form,})
    # else:
    #     form = ContactForm()
    #     if 'submitted' in request.GET:
    #         submitted = True
    return render(request, 'servicesapp/services_api.html', {})

def email_inquiry(name, email, message, serviceType, phone=None, date=None,):
    msg_plain = render_to_string('servicesapp/email_inquiry.txt', {'contactName':name, 'contactEmail':email, 'contactPhone':phone, 'contactDate':date, 'contactMessage':message,})
    msg_html = render_to_string('servicesapp/email_inquiry.html', {'contactName':name, 'contactEmail':email, 'contactPhone':phone, 'contactDate':date, 'contactMessage':message,})
    send_mail(subject=serviceType,message=msg_plain,from_email=settings.EMAIL_HOST_USER, recipient_list=[settings.EMAIL_HOST_USER], html_message=msg_html)

def beta(request):
    return render(request, 'servicesapp/contact.html', {})

# Create your views here.
