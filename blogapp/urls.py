from django.urls import path
from django.conf import settings
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home, name='bloghome'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('settimezone', views.settimezone, name='settimezone')
    # path("accounthome", views.AccountHome, name="accounthome"), # django-allauth login endpoint

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)