from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import *
from Recipe_adminapp . models import *
from django.contrib import admin



# Create your views here.
def userindex1(request):
    data=recipe.objects.all()
    return render(request,'userindex1.html',{'data':data})
def recipe_detail(request,id):
    data=recipe.objects.filter(id=id)
    return render(request,'recipe_detail.html',{'data':data})
def usercontact(request):
    return render(request,'contact.html')
def getData(request):
    if request.method=="POST":
        name_a = request.POST.get('name1')
        email_a= request.POST.get('email1')
        message_a= request.POST.get('message1')
       
        data=contact(name1=name_a,email1=email_a,message1=message_a)
        data.save()
        return redirect('usercontact')


def userregister(request):
    return render(request,'register.html')
def registerdata(request):
    if request.method=="POST":
        name = request.POST.get('name')
        email_a= request.POST.get('email')
        password_a= request.POST.get('password')
        if name== "" or email_a=="" or password_a=="":
            return redirect('userregister')
        data=register(name=name,email=email_a,password=password_a)
        data.save()
        return redirect('login')
    
            
        
def login(request):
    return render(request,'userlogin.html')
def userlogin(request):
    if request.method == "POST":
        username=request.POST.get('name')
        password_a=request.POST.get('password')
        if register.objects.filter(name=username,password=password_a).exists():
            data=register.objects.filter(name=username,password=password_a).values('email','id').first()
            request.session['email'] = data['email']
            request.session['name'] = username
            request.session['password'] = password_a
            request.session['nid'] = data['id']
            return redirect('userindex1')
        else:
            
            return render(request,'userlogin.html',{'msg':"invalid"})
          
    else:
        return render(request,'userlogin.html')

    
def logout(request):
    del request.session['email']
    del request.session['name']
    del request.session['password']
    del request.session['nid']
    return redirect('userindex1')
     
def usercontact(request):
    return render(request,'contact.html')
def getData(request):
    if request.method=="POST":
        name_a = request.POST.get('name1')
        email_a= request.POST.get('email1')
        message_a= request.POST.get('message1')
       
        data=contact(name1=name_a,email1=email_a,message1=message_a)
        data.save()
        return redirect('usercontact')       

    

