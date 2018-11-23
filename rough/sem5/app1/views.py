from django.shortcuts import render
from django.http import HttpResponse
from sem5 import dbconnection
#from labreport import cstructure
from django.http import HttpResponseRedirect
from django.template import RequestContext
#Public Views

def login(request):
    if request.method=='POST':
        a=request.POST.get('u')
        b=request.POST.get('p')
        
        sql="select * from login where name='"+a+"' and psd='"+b+"'"
        data=dbconnection.selectdata(sql) 
        if data:                        
            if data[1]==a and data[2]==b:
                print("login successfull")
                return HttpResponseRedirect("http://127.0.0.1:8000/bank")
            else:
                print("login failed")
                return HttpResponseRedirect("http://127.0.0.1:8000/logfail")
        else:
            print("Login failed")    
            return HttpResponseRedirect("http://127.0.0.1:8000/logfail")
    
    return render(request,"login.html",{})

def bank(request):
    return render(request,"bank.html",{})
    
def logfail(request):
        return render(request,"logfail.html",{})
def about(request):
    return render(request,"about.html",{})