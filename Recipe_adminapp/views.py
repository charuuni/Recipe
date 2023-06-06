from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import *
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from Recipe_userapp . models import *


# Create your views here.
def adminindex(request):
    recipe1=recipe.objects.all().count()
    register1=register.objects.all().count()
    contact1=contact.objects.all().count()
    return render(request,'adminindex.html',{'recipe':recipe1,'register':register1,'contact':contact1})
    
def add(request):
    return render(request,'add_recipe.html')
def recipedata(request):
    if request.method=="POST":
        recipe_name=request.POST.get('recipe_name')
        recipe_image=request.FILES['recipe_image']
        instruction=request.POST.get('instruction')
        ingredients=request.POST.get('ingredients')

        data=recipe(recipe_name=recipe_name,recipe_image=recipe_image,instruction=instruction,ingredients=ingredients)
        data.save()
        return redirect('messages')
def messages(request):
    data=recipe.objects.all()
    return render(request,'messages.html',{'key':data})
def view_recipe(request,id):
    data=recipe.objects.filter(id=id)
    return render(request,'view_recipe.html',{'data':data})
def update(request,id):
    if request.method=='POST':
        recipe_name=request.POST['recipe_name']
        instruction=request.POST['instruction']
        ingredients=request.POST['ingredients']
        try:
            recipe_image=request.FILES['recipe_image']
            fs = FileSystemStorage()
            file = fs.save(recipe_image.name, recipe_image)
        except MultiValueDictKeyError:
            file =recipe.objects.get(id=id).recipe_image

        data=recipe.objects.filter(id=id).update(recipe_name=recipe_name,instruction=instruction,ingredients=ingredients,recipe_image=recipe_image)
        return redirect('messages')
def delete(request,id):
    data=recipe.objects.filter(id=id).delete()
    return redirect('messages')
   
def viewcontact(request):
    data=contact.objects.all()
    return render(request,'viewcontact.html',{'data':data})
def users(request):
    data=register.objects.all()
    return render(request,'users.html',{'data':data})




