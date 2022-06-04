
from django.urls import path
from . import views

urlpatterns = [
    path('set/', views.set_cookies, name="set_cookies"),
    path('get/', views.get_cookies, name="get_cookies"),
    path('del/', views.del_cookies, name="del_cookies"),
    path('sign/set/', views.set_sign_cookies, name="set_sign_cookies"),
    path('sign/get/', views.get_sign_cookies, name="get_sign_cookies"),
    path('sign/del/', views.del_sign_cookies, name="del_sign_cookies"),
]
