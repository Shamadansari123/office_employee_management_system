from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Department,Role,Employee
from django.contrib import messages
from datetime import datetime
# Create your views here.
def index(request):
    return render(request,'emp_app/index.html')


def all_emp(request):
    emps=Employee.objects.all()
    return render(request,'emp_app/all.html',{"emps":emps})


def add_emp(request):
    if request.method=="POST":
        fn=request.POST['first_name']
        ln=request.POST['last_name']
        dp=int(request.POST['dept'])
        sal=request.POST['salary']
        bo=request.POST['bonus']
        ro=int(request.POST['role'])
        ph=request.POST['phone']
        emp=Employee(first_name=fn,last_name=ln,dept_id=dp,salary=sal,bonus=bo,role_id=ro,phone=ph,join_date=datetime.now())
        emp.save()
        messages.success(request,"New Employee Added Successfully..!!!")
        return HttpResponseRedirect("/all")
    else:
        return render(request,'emp_app/add.html')


def remove_emp(request,emp_id=0):
    if emp_id:
        emp=Employee.objects.get(id=emp_id)
        emp.delete()
        messages.success(request,"Employee Deleted..!!")
        return HttpResponseRedirect('/all/')
    else:
        emps=Employee.objects.all()
        return render(request,'emp_app/remove.html',{"emps":emps})


def filter_emp(request):
    if request.method=="POST":
        fn=request.POST['first_name']
        ln=request.POST['last_name']
        dp=request.POST['dept']
        ro=request.POST['role']
        if fn:
            emp=Employee.objects.filter(first_name__iexact=fn)
        if ln:
            emp=Employee.objects.filter(last_name__iexact=ln)
            
        if dp:
            emp=Employee.objects.filter(dept__name__iexact=dp)
            
        if ro:
            emp=Employee.objects.filter(role__name__iexact=ro)

        return render(request,'emp_app/filter.html',{"emp":emp})
    else:
        return render(request,'emp_app/filter.html')