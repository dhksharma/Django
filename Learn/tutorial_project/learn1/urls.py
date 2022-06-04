
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('contact/', views.contact, name="contact"),
    path('about/', views.about, name="about"),
    path('route-param/', views.route_param, name="route_param"),
    path(
        'route-param/<int:id>/<str:name>',
        views.parameter_method,
        name="parameter_method"
    ),
    path(
        'route-param/json-data/<str:json_data>',
        views.json_data,
        name="json_data"
    ),
    path(
        'route-param/call-get-ajax/',
        views.call_get_ajax,
        name="call_get_ajax"
    ),
    path(
        'route-param/call-post-ajax/',
        views.call_post_ajax,
        name="call_post_ajax"
    ),


    
]
