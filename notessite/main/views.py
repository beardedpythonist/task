from django.shortcuts import render, redirect

from .forms import TaskForm
from .models import *

def index(request):
    task = Task.objects.all()
    context = {'task': task}
    return render(request, 'main/index.html', context)

def about(request):
    return render(request, 'main/about.html')



def create(request):
    error = ''
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Error'
    form = TaskForm()

    context ={'form': form, 'error': error}
    return render(request, 'main/create.html', context)