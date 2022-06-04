from dataclasses import fields
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomClass(UserCreationForm):

  class Meta:
      model = User
      fields = "__all__"
