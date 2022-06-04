from email.policy import default
from unicodedata import name
from django.db import models

# Create your models here.


class AddTimeStamp(models.Model):
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  #If we will not provide this Meta class than a table for this AddTimeStamp class also get generated
  class Meta:
    abstract = True


class Student(AddTimeStamp):
  name = models.CharField(max_length=100, null=True)
  email = models.EmailField(max_length=100, unique=True)
  password = models.CharField(max_length=100)
  usertype = models.IntegerField(default=0)

#This function is just to show name in admin pannel we can change it to any column name as example email, password etc.
  # def __str__(self):
  #     return self.name


class Details(AddTimeStamp):
  student = models.ForeignKey(Student, on_delete=models.CASCADE)
  phone = models.BigIntegerField(null=True)

  # def __str__(self):
  #     return self.phone


