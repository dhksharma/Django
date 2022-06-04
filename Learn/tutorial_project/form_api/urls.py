
from django.urls import path
from . import views

urlpatterns = [
    path('', views.form_api, name="form_api"), 
    path('stu-reg', views.stu_reg, name="stu_reg"), 
    path('form-render', views.form_render, name="form_render"), 
    path('form-loop', views.form_loop, name="form_loop"), 
    path('field-args', views.field_args, name="field_args"), 
    path('widget', views.widget, name="widget"), 
    path('form-validate', views.form_validate, name="form_validate"), 
    path('redirect-url', views.redirect_url, name="redirect_url"), 
    path('custom-form-validate', views.custom_form_validate, name="custom_form_validate"), 
]
