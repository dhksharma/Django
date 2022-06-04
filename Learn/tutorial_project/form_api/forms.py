import email
from unicodedata import name
from xml.dom.minidom import Attr
from django import forms


class StudentRegistration(forms.Form):
  name = forms.CharField(initial="Sharma")
  email = forms.EmailField(help_text="This is help text")


class StuReg(forms.Form):
  l_name = forms.CharField()
  f_name = forms.CharField()
  email = forms.EmailField()


class FormLoop(forms.Form):
  l_name = forms.CharField()
  f_name = forms.CharField()
  email = forms.EmailField()
  mobile = forms.IntegerField()
  password = forms.CharField(widget=forms.HiddenInput())


class FieldArgs(forms.Form):
  name = forms.CharField(
      label='Your Name',
      label_suffix='  ',
      initial='Sharma',
      required=False,
      disabled=True,
      help_text='Please provide valid details'
  )


class CustomWidget(forms.Form):
  name = forms.CharField(widget=forms.TextInput(
      attrs={'class': "custom_class", 'id': 'custom_id'}))
  password = forms.CharField(widget=forms.PasswordInput())
  address = forms.CharField(widget=forms.Textarea())
  checkbox = forms.CharField(widget=forms.CheckboxInput())
  File = forms.CharField(widget=forms.FileInput())


class FormValidation(forms.Form):
  name = forms.CharField(widget=forms.TextInput(
      attrs={'class': "custom_class", 'id': 'custom_id'}))
  password = forms.CharField(widget=forms.PasswordInput())
  address = forms.CharField(widget=forms.Textarea())
  checkbox = forms.CharField(widget=forms.CheckboxInput())
  # file = forms.CharField(widget=forms.FileInput())

def start_with_d(param):
  if param[0] != 'd' and param[0] != 'D':
    raise forms.ValidationError("F name doesnot starts with d")

class Registration(forms.Form):
  f_name = forms.CharField(validators=[start_with_d])
  name = forms.CharField()
  email = forms.EmailField()
  password = forms.CharField(widget=forms.PasswordInput())
  confirm_password = forms.CharField(widget=forms.PasswordInput())

  #This function is used when we have to validate all form fields else use below one for specific fields
  def clean(self):
    cleaned_data = super().clean()

    print("=======cleaned_data======",cleaned_data)
    name_val = cleaned_data['name']
    print("=======name_val======",name_val)
    email_val = cleaned_data.get('email')

    print("=======email_val======",email_val)
    password_val = cleaned_data.get('password')
    confirm_password_val = cleaned_data.get('confirm_password')

    if email_val and len(email_val) < 8:
      raise forms.ValidationError("Enter email greater than 8 chars")
    
    if len(name_val) < 8:
      raise forms.ValidationError("Enter name greater than 8 chars")

    if (confirm_password_val and confirm_password_val) != (password_val and password_val):
      raise forms.ValidationError("password and confirm password is not same")

  # def clean_name(self):
  #   # name=self.cleaned_data.get('name') # both line are same
  #   nameVal = self.cleaned_data['name']

  #   print("====nameVal====", nameVal)

  #   #If name less than 4 char then error will br raised else name will be returned
  #   if len(nameVal) < 8:
  #     raise forms.ValidationError("Enter name greater than 8 chars")
  #   return nameVal
