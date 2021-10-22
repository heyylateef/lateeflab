from django.urls import path
from django.conf import settings
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home, name='home'),
    path('pricing', views.pricing, name='pricing'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('services_ecommerce', views.services_ecommerce, name='services_ecommerce'),
    path('services_api', views.services_api, name='services_api'),
    path('contact', views.contact, name="contact"),
    path('about', views.about, name="about"),
    #path('contact_us_form', views.contact_us_form, name='contact_us_form'),
    path('privacypolicy', views.privacypolicy, name='privacypolicy'),
    path('termsandconditions', views.termsandconditions, name='termsandconditions'),
    path('beta', views.beta, name='beta'),
    # path('menu',views.menu, name='menu'),
    # path('settimezone', views.settimezone, name='settimezone'),
    # path("accounthome", views.AccountHome, name="accounthome"), # django-allauth login endpoint

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)