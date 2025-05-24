from django.shortcuts import render
from django.http import HttpResponse
from .forms import StudentModelForm


def home(req):
    if req.method == "POST":
        form = StudentModelForm(data=req.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('subi')

    form = StudentModelForm()
    return render(req,"f1/new_index.html",{'forms':form})