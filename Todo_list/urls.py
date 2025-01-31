from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("tags/", views.tag_list, name="tag_list"),
    path('add-task/', views.add_task, name='add_task'),
    path("task/update/<int:pk>/", views.update_task, name="update_task"),
    path("task/delete/<int:pk>/", views.delete_task, name="delete_task"),
    path("task/toggle/<int:pk>/", views.toggle_task_status, name="toggle_task_status"),
    path('add-tag/', views.add_tag, name='add_tag'),
    path("tag/update/<int:pk>/", views.update_tag, name="update_tag"),
    path("tag/delete/<int:pk>/", views.delete_tag, name="delete_tag"),
    ]
app_name = 'todo'