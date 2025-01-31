from django.urls import path
from . import views

app_name = "todo"

urlpatterns = [
    path("", views.home, name="home"),
    path("add-task/", views.add_task, name="add_task"),
    path("update-task/<int:pk>/", views.update_task, name="update_task"),
    path("delete-task/<int:pk>/", views.delete_task, name="delete_task"),
    path("toggle-task-status/<int:pk>/", views.toggle_task_status, name="toggle_task_status"),
    path("tags/", views.tag_list, name="tag_list"),
    path("add-tag/", views.add_tag, name="add_tag"),
    path("update-tag/<int:pk>/", views.update_tag, name="update_tag"),
    path("delete-tag/<int:pk>/", views.delete_tag, name="delete_tag"),
]
