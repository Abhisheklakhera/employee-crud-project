from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def homeview(request):
    return render(request,'home.html')

def detailsview(request):
    name=request.POST['empname']
    email=request.POST['email']
    result="The name is:"+str(name)+"<br>"+"The email is:"+str(email)
    return HttpResponse(result)

def empformview(request):
    return render(request,'employeeform.html')