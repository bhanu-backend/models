from django.shortcuts import render
from .models import Employee

def app2_home(req):
    data = Employee.objects.all()
    return render(req,"app2/newindex.html",{'data':data})
