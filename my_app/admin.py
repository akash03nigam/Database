from django.contrib import admin
from my_app.models import Student
from my_app.models import Employee

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['Eno','Ename','Escore']

class StudentAdmin(admin.ModelAdmin):
    list_display=['Sno','Sname','Sscore']

admin.site.register(Student,StudentAdmin)
admin.site.register(Employee,EmployeeAdmin)
