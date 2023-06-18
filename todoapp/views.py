from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import TaskForm
from .models import Task

# Create your views here.

@login_required(login_url="members/login/")
def home(request):
    form = TaskForm()
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = Task(user = request.user, text = form.cleaned_data["text"])
            task.save()
            messages.success(request, ("Task was added!"))
            return redirect("home")
        else:
            messages.error(request, ("Invalid form!"))
            return redirect("home")
    current_user = request.user
    tasks = current_user.task_set.all()
    return render(request, "todoapp/tasks.html", {"tasks":tasks, "form":form})

@login_required(login_url="members/login/")
def update_task(request, id):
    task = Task.objects.get(id = id)
    form = TaskForm(instance = task)

    if request.method == "POST":
        form = TaskForm(request.POST, instance = task)
        if form.is_valid():
            form.save()
            messages.success(request, ("Updated successfully!"))
            return redirect("home")
        else:
            messages.error(request, ("Invalid form!"))
            return redirect("home")

    return render(request, "todoapp/update.html", {"form":form})

@login_required(login_url="members/login/")
def delete_task(request, id):
    if request.method == "POST":
        task = Task.objects.get(id = id)
        task.delete()
        messages.success(request, ("Deleted successfully!"))
        return redirect("home")
    
    return render(request, "todoapp/delete.html")

