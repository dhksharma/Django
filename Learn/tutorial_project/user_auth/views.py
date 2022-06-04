from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .forms import CustomClass
from django.contrib.auth import authenticate, login as dj_login, logout

# Create your views here.


def index(request):
  if request.method == 'POST':
    form_obj = UserCreationForm(request.POST)
    if form_obj.is_valid():
      # to save data in table
      form_obj.save()
      print(form_obj.cleaned_data)
  else:
    form_obj = UserCreationForm()

  return render(request, 'user_auth/index.html', {"form": form_obj})


def all_fields(request):
  if request.method == 'POST':
    form_obj = CustomClass(request.POST)
    if form_obj.is_valid():
      print(form_obj.cleaned_data)
  else:
    form_obj = CustomClass()

  return render(request, 'user_auth/index.html', {"form": form_obj})


def login(request):
  if request.method == 'POST':
    form_obj = AuthenticationForm(request=request, data=request.POST)
    if form_obj.is_valid():
      username = form_obj.cleaned_data.get('username')
      password = form_obj.cleaned_data.get('password')
      user = authenticate(username=username, password=password)

      if user is not None:
        print(user)
        dj_login(request, user)
        return redirect("profile", user.id)
  else:
    form_obj = AuthenticationForm()

  return render(request, 'user_auth/login.html', {"form": form_obj})


def profile(request, u_id):

  if request.user.is_authenticated:
    return render(
        request,
        'user_auth/profile.html',
        {
            "id": u_id,
            "name": request.user,
            # "email": request.user.email,
        }
    )
  else:
    return redirect('login')


def logout_user(request):
  logout(request)
  return redirect('login')
