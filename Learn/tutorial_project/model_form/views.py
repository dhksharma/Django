from email import message
from django.http.response import HttpResponse
from django.shortcuts import render
from .form import *
from .models import *
from django.contrib import messages

# Create your views here.


def index(request):
  if request.method == 'POST':
    model_obj = CustomModelForm(request.POST)

    if model_obj.is_valid():
      print(model_obj.cleaned_data)

      #This is the way to Insert data
      user_model_obj = User(
          name=model_obj.cleaned_data.get('name'),
          email=model_obj.cleaned_data.get('email'),
          password=model_obj.cleaned_data.get('password'),
      )
      user_model_obj.save()
      #this message will work as flash message
      messages.add_message(request,messages.SUCCESS,"User details added successfully")
      #This is the way to Update data
      # user_model_obj = User(
      #     id=1,
      #     name=model_obj.cleaned_data.get('name'),
      #     email=model_obj.cleaned_data.get('email'),
      #     password=model_obj.cleaned_data.get('password'),
      # )
      # user_model_obj.save()

      #This is the way to delete data
      # user_model_obj = User(
      #     id=1
      # )
      # user_model_obj.delete()
      # return HttpResponse("<h1>VALID FORM</h1>")
  else:
    model_obj = CustomModelForm()
    #This message will work as flash message we can return multiple message
    messages.add_message(request,messages.SUCCESS,"Add new user")
    print(messages.get_level(request))
    messages.info(request,"Info message")

    #this debug will not print as it has 10 level after set level this will print
    #level below 20 will not print by default for that we have to set it first
    messages.debug(request,"Debug message")
    messages.set_level(request,messages.DEBUG)
    messages.debug(request,"Debug message")
    print(messages.get_level(request))

  return render(request, 'model_form/index.html', {'form': model_obj})


def message_fun(request):

  messages.info(request,"Info message")
  messages.success(request,"Success message")
  messages.warning(request,"Warning message")
  messages.debug(request,"Debug message")
  messages.error(request,"Error message")
  return render(request,'model_form/show_message.html')