from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, Tag
from .forms import TaskForm, TagForm
from django.utils import timezone

def home(request):
    tasks = Task.objects.all().order_by("is_done", "-created_at")
    form = TaskForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("todo:home")
    return render(request, "home.html", {"tasks": tasks, "form": form})


def add_task(request):
    form = TaskForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("todo:home")
    return render(request, "add_task.html", {"form": form})

def update_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("todo:home")
        else:
            print("Form errors:", form.errors)  # Виведення помилок форми для налагодження
    else:
        form = TaskForm(instance=task)
    return render(request, "update_task.html", {"form": form})



def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        task.delete()
        return redirect("todo:home")
    return render(request, "delete_task.html", {"task": task})

def toggle_task_status(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_done = not task.is_done
    task.save()
    return redirect("todo:home")

def tag_list(request):
    tags = Tag.objects.all()
    return render(request, "tag_list.html", {"tags": tags})

def add_tag(request):
    form = TagForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("todo:tag_list")
    return render(request, "add_tag.html", {"form": form})

def update_tag(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    form = TagForm(request.POST or None, instance=tag)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("todo:tag_list")
    return render(request, "update_tag.html", {"form": form})

def delete_tag(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    if request.method == "POST":
        tag.delete()
        return redirect("todo:tag_list")
    return render(request, "delete_tag.html", {"tag": tag})
