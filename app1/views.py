from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Employee
def home(request):
    data = Employee.objects.all()
    if request.method == "POST":
        nm = request.POST.get('name')
        age = request.POST.get('age')
        email = request.POST.get('email')
        designation = request.POST.get('desig')
        print(nm,age,email,designation)
        print(request.POST)
        Employee.objects.create(name=nm,email=email,age=age,designation=designation)
        #return HttpResponse("data submitted")
        return HttpResponseRedirect('/')
   
    return render(request,'app1/index.html',{'data':data})



def delete_data(request,id):
    data = Employee.objects.get(pk=id)
    data.delete()
    return HttpResponseRedirect('/')
   