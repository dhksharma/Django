from django.http.response import HttpResponse
from django.shortcuts import render
from form_api.forms import *
from django.http import HttpResponseRedirect

# Create your views here.


def form_api(request):
  form_obj = StudentRegistration()
  context = {
      "form": form_obj
  }
  return render(request, 'form_api/stu_reg.html', context)


def stu_reg(request):
  form_obj = StuReg(auto_id='any_name_%s', initial={'f_name': 'Dharmendra'})
  form_obj1 = StuReg(
      auto_id=True,
      label_suffix='-',
      initial={
          'l_name': 'Sharma',
          'email': 'abc@gmail.com'
      },
      field_order=['f_name', 'l_name']
  )
  form_obj2 = StuReg(auto_id="ant_string")  # this will also act as True
  form_obj3 = StuReg(auto_id=False)
  context = {
      "form_obj": form_obj,
      "form_obj1": form_obj1,
      "form_obj2": form_obj2,
      "form_obj3": form_obj3,
  }
  return render(request, 'form_api/stu_reg_custom.html', context)


def form_render(request):
  form_obj = StudentRegistration()
  context = {
      "form": form_obj
  }
  return render(request, 'form_api/form_render.html', context)


def form_loop(request):
  form_obj = FormLoop()
  context = {
      "form": form_obj
  }
  return render(request, 'form_api/form_loop.html', context)


def field_args(request):
  form_obj = FieldArgs()
  context = {
      "form": form_obj
  }
  return render(request, 'form_api/field_args.html', context)


def widget(request):
  form_obj = CustomWidget()
  context = {
      "form": form_obj
  }
  return render(request, 'form_api/widget.html', context)


def form_validate(request):

  if request.method == 'POST':
    print(request.POST.dict())
    form_obj = FormValidation(request.POST)
    if form_obj.is_valid():
      print("Form data")
      print("name", form_obj.cleaned_data['name'])

      return HttpResponseRedirect('redirect_url')
  else:
    form_obj = FormValidation()
  context = {
      "form": form_obj
  }
  return render(request, 'form_api/form_validate.html', context)


def redirect_url(request):
  return HttpResponse("<h1>Form submitted successfully</h1>")


def custom_form_validate(request):

  if request.method == 'POST':

    form_obj = Registration(request.POST)
    if form_obj.is_valid():
      return HttpResponse("POST METHOD")
  else:
    form_obj = Registration()

  return render(
      request,
      'form_api/custom_form_validation.html',
      {
          'form': form_obj
      }
  )
