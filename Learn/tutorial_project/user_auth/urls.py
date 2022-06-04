
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('all-fields', views.all_fields, name="all_fields"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout_user, name="logout_user"),
    path('user-profile/<u_id>', views.profile, name="profile"),
]
