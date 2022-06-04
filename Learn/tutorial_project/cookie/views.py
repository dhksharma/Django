from email.policy import default
from django.shortcuts import render

# Create your views here.


def set_cookies(request):
  response = render(request, 'cookie/setcookie.html')
  response.set_cookie("name", 'Dharmendra', max_age=100)  # max_age in seconds
  return response


def get_cookies(request):
  name = request.COOKIES.get('name', 'Cookies not found')
  return render(request, 'cookie/getcookie.html', {'data': name})


def del_cookies(request):

  response = render(request, 'cookie/delcookie.html')
  response.delete_cookie("name")
  return response

#Signed cookie is used for security purpose


def set_sign_cookies(request):
  response = render(request, 'cookie/setcookie.html')
  response.set_signed_cookie(
      "name", 'Dharmendra', salt="anysalt", max_age=100)  # max_age in seconds
  return response


def get_sign_cookies(request):
  name = request.get_signed_cookie("name", default="default value", salt='anysalt')
  return render(request, 'cookie/getcookie.html', {'data': name})


def del_sign_cookies(request):

  response = render(request, 'cookie/delcookie.html')
  response.delete_cookie("name")
  return response
