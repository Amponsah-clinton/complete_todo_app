from django.shortcuts import render, redirect
from .models import myapp
from .forms import TodoForm

# Create your views here.

def index(request):
    form = TodoForm()
    obj = myapp.objects.all()
    if request.method =='POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            form = TodoForm()

    return render(request,'index.html',{'form':form, 'obj':obj})

def Update(request, id):
    obj = myapp.objects.get(id=id)
    form = TodoForm()
    if request.method =='POST':
        form = TodoForm(request.POST, instance = obj)
        if form.is_valid():
            form.save()
            form = TodoForm()
            return redirect('/')

    return render(request,'update.html',{'form':form, 'obj':obj})

def Delete(request, id):
    obj = myapp.objects.get(id=id)
    obj.delete()
    return redirect('/')










