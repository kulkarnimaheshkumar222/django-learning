from django.urls import path
from .views import home, add_task, task_detail,edit_task, delete_task,toggle_task

urlpatterns =[
    path("", home),
    path("add/",add_task),
    path("task/<int:id>/", task_detail),
    path("task/<int:id>/edit/", edit_task),
    path("task/<int:id>/delete/", delete_task),
    path("task/<int:id>/toggle/", toggle_task),
]