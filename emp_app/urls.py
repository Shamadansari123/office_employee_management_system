from django.contrib import admin
from django.urls import path
from emp_app import views


urlpatterns = [
    path("",views.index,name="index"),
    path("all/",views.all_emp,name="allemp"),
    path("add/",views.add_emp,name="addemp"),
    path("remove/",views.remove_emp,name="removeemp"),
    path("remove/<int:emp_id>",views.remove_emp,name="removeemp"),
    path("filter/",views.filter_emp,name="filteremp"),
]
