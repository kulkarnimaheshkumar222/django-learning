from django.shortcuts import render
from .models import Task

def home(request):
    my_tasks = Task.objects.all()

    return render(request, "todo_app/home.html", {
        "tasks": my_tasks
    })

    return render(request,"todo_app/home.html")
