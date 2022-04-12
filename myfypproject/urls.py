"""myfypproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from lipreading.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', initial_view, name = 'initial'),
    path('home', home_view, name = 'home'),
    path('login', auth_views.LoginView.as_view(template_name = 'login.html'), name = 'login'),
    path('detect_mouth', mouth_detect_view, name = 'home'),
    path('correction_module', correction_module_view, name = 'home'),
    path('correction_module_use', correction_module_view_use, name = 'home'),
    path('feedback_module/<str:corrected_text>', feedback_module_view, name = 'feedback'),
    path('mix_module/<str:speaker>', mix_module_view, name = 'mix'),
    path('new_final_output', new_final_output_view, name = 'f_output'),
    path('contact_us', contact_us_view, name = 'contact_us'),
    path('about_us', about_us_view, name = 'about_us'),

    path('admin/', admin.site.urls),
]
urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)