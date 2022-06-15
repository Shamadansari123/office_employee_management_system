from django.contrib import admin
from emp_app.models import Department,Role,Employee
# Register your models here.

@admin.register(Department)
class Deptadmin(admin.ModelAdmin):
    list_display=['id','name','location']


@admin.register(Role)
class Roleadmin(admin.ModelAdmin):
    list_display=['id','name']


@admin.register(Employee)
class Empadmin(admin.ModelAdmin):
    list_display=['id','first_name','last_name','dept','salary','bonus','role','phone','join_date']