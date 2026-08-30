from django.shortcuts import render, redirect
from .models import Task

def home(request):
    my_tasks = Task.objects.all()

    return render(request, "todo_app/home.html", {
        "tasks": my_tasks
    })

    return render(request,"todo_app/home.html")

def add_task(request):

    if request.method == "POST":
        title = request.POST["title"]
        description = request.POST["description"]

        Task.objects.create(
            title=title,
            description=description
        )

        return redirect("/")

    return render(request, "todo_app/add_task.html")

def task_detail(request, id):
    task = Task.objects.get(id=id)

    return render(request, "todo_app/task_detail.html", {
        "task": task
    })

def edit_task(request, id):

    task = Task.objects.get(id=id)

    if request.method == "POST":
        task.title = request.POST["title"]
        task.description = request.POST["description"]

        task.save()

        return redirect(f"/task/{task.id}/")

    return render(request, "todo_app/edit_task.html", {
        "task": task
    })

def delete_task(request, id):

    task = Task.objects.get(id=id)

    if request.method == "POST":
        task.delete()
        return redirect("/")

    return redirect(f"/task/{task.id}/")