"""predict URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import url,include
from django.contrib.auth import views as auth_view
from ml.views import Index

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',Index.as_view(),name='index'),
    url(r'^Login', auth_view.LoginView.as_view(template_name="login.html"), name='login'),
    url(r'^Logout', auth_view.LogoutView.as_view(), name='logout'),
    url(r'^ml/',include('ml.urls')),
]
