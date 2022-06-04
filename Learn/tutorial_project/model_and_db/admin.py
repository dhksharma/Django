from django.contrib import admin
from model_and_db.models import *

# Register your models here.

#By using decorator also we can show data in tabular form in admin section
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
  list_display=('id','name','email','password','usertype','created_at','updated_at')

#This will help to show data in tabular form in admin section
# class StudentAdmin(admin.ModelAdmin):
#   list_display=('id','name','email','password','usertype','created_at','updated_at')
# admin.site.register(Student,StudentAdmin)


admin.site.register(Details)



