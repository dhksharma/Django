"""tutorial_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from xml.etree.ElementInclude import include
from django import urls
from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('learn.urls')),
    path('learn/', include('learn.urls')),
    path('learn1/', include('learn1.urls')),
    path('model-db/', include('model_and_db.urls')),
    path('form-api/', include('form_api.urls')),
    path('model-form/', include('model_form.urls')),
    path('user-auth/', include('user_auth.urls')),
    path('cookie/', include('cookie.urls')),
    path('session/', include('session.urls')),
]
