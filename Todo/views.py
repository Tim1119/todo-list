from django.shortcuts import render
from .forms import TodoForm
from .models import Todo
from django.shortcuts import redirect,get_object_or_404
from django.views.generic import CreateView
# Create your views here.
def HomeView(request):
    all_items = Todo.objects.all()
    form = TodoForm()
    print('POST COMPLETE')
    if request.method  == "POST":
        print('POST COMPLETE POSTTTTTT')
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return redirect('home')
    return render(request,'Todo\index.html',{'form':form,'all_items':all_items})

def DeleteView(request,pk):
    item = get_object_or_404(Todo,id=pk)
    item.delete()
    return redirect('home')
    return render(request,'Todo\index.html')

def EditView(request,pk):
    all_items = Todo.objects.all()
    item = get_object_or_404(Todo,id=pk)
    form = TodoForm(instance=item)
    if request.method  == "POST":
        form = TodoForm(request.POST,instance=item)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return redirect('home')
    return render(request,'Todo\edit.html',{'form':form,'all_items':all_items})

def CompletedView(request,pk):
    
    item = get_object_or_404(Todo,id=pk)
    item.completed = True
    item.save()
    form = TodoForm()
    print('POST COMPLETE')
    if request.method == "POST":
        print('POST COMPLETE')
    return render(request,'Todo\index.html')