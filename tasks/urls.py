from django.urls import path
from . import views

urlpatterns = [
    path('',  views.signin),
    path('tasks/', views.tasks, name="tasks"),
    path('projects/', views.projects, name="projects"),
    path('project_view/<int:project_id>/', views.project_view, name="project_view"),
    path('signup/', views.signup, name="signup"),
    path('signin/', views.signin, name="signin"),
    path('signout/', views.signout, name="signout"),
    path('create_task/id_project=<int:project_id>/', views.create_task, name="create_task"),
    path('create_project/', views.create_project, name="create_project")
]