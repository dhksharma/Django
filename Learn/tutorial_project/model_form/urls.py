
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('msg/', views.message_fun, name="message"),
]
