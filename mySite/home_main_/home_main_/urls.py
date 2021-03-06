"""home_main_ URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path,include
from django.contrib.auth import views as auth_views
from enquiry_users import views 

urlpatterns = [
    path('',include('home.urls')),
    path('profile/',include('user.urls')),
    path('enquiry/',views.enquiry,name='enquiry'),
    path('admin/', admin.site.urls),
    path('profile/login/',auth_views.LoginView,name='login'),
    path('profile/logout/',auth_views.LogoutView,name='logout'),
    path('oauth/',include('social_django.urls',namespace='social')),

]
