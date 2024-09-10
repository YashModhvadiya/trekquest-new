from django.urls import path
from home import views
from .views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = 'home'

urlpatterns = [
    path('customer-registration/', views.resregister, name='resregister'),  
    path('customer-login/', views.reslogin, name='reslogin'), 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)