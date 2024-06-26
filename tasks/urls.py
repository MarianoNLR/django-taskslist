from django.urls import path
from . import views

urlpatterns = [
    path('',  views.signin),
    #path('task_view/', views.tasks, name="task_view"),
    path('projects/', views.projects, name="projects"),
    path('project_view/<int:project_id>/', views.project_view, name="project_view"),
    path('signup/', views.signup, name="signup"),
    path('signin/', views.signin, name="signin"),
    path('signout/', views.signout, name="signout"),
    path('create_task/id_project=<int:project_id>/', views.create_task, name="create_task"),
    path('create_project/', views.create_project, name="create_project"),
    path('projects/delete_project/<int:project_id>/', views.delete_project, name="delete_project"),
    path('delete_task/<int:task_id>/', views.delete_task, name="delete_task"),
    path('update_project/<int:project_id>', views.update_project, name="update_project"),
    path('update_task/<int:task_id>', views.update_task, name="update_task")
]