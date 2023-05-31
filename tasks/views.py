from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import CreateTaskForm, CreateProjectForm
from .models import Project, Task
# Create your views here.
def hello(request):
    return HttpResponse("<h1>Hello World</h1>")

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html',{
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(username=request.POST['username'],
            password=request.POST['password1'])
            user.save()
            return HttpResponse('Usuario creado con exito')

def signout(request):
    logout(request)
    return redirect('signin')
   
def signin(request):
    if request.user.id is not None:
        return redirect('projects')
    
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            username = request.POST['username'], password = request.POST['password']
        )
        if user is None:
            return render(request, 'signin.html', {
            'form': AuthenticationForm,
            'error': 'Username or password incorrect'
        })
        else:
            login(request, user)
            return redirect('projects')
        
@login_required
def tasks(request):
    return render(request, 'tasks.html')

@login_required
def projects(request):
    projects = Project.objects.filter(user=request.user)
    list_task = []
    for project in projects:
        task = Task.objects.filter(project_id=project.id)
        task_count = task.filter(done=True).count()
        project.count = f'{task_count}/{task.filter().count()}'
    print(list_task)
    
        
    return render(request, 'projects.html', {
        'projects': projects,
        'list_task': list_task
    })
    
def project_view(request, project_id):
    project = Project.objects.filter(id=project_id).first()
    print(project)
    if project is None:
        return redirect('projects')
    if project.user_id != request.user.id:
        return redirect('projects')
    else:
        tasks = Task.objects.filter(project_id=project_id)
        return render(request, 'project_view.html', {
            'project': project,
            'tasks': tasks
        })
    

@login_required
def create_task(request, project_id):
    project = Project.objects.filter(id=project_id).first()
    print(project_id)
    if project.user_id != request.user.id:
        return redirect('projects')
    
    
    if request.method == 'GET':
        return render(request, 'create_task.html', {
            'form': CreateTaskForm
        })
    else:
        print(request.POST)
        form = CreateTaskForm(request.POST)
        new_task = form.save(commit=False)
        new_task.project_id = project_id
        new_task.save()
        return redirect('project_view', project_id=project_id)
    
@login_required
def create_project(request):
    if request.method == 'GET':
        return render(request, 'create_project.html', {
            'form': CreateProjectForm
        })
    else:
        form = CreateProjectForm(request.POST)
        new_project = form.save(commit=False)
        new_project.user = request.user
        new_project.save()
        return redirect('projects')

@login_required
def delete_project(request, project_id):
    instance = Project.objects.get(id=project_id)
    if request.user.id == instance.user_id:
        instance.delete() 
    return redirect('projects')

@login_required
def delete_task(request, task_id):
    instance = Task.objects.get(id=task_id)
    if instance is not None:
        instance.delete()
        return redirect('project_view', project_id=instance.project_id)

def update_project(request, project_id):
    if request.method == 'GET':
        project = Project.objects.get(id=project_id)
        form = CreateProjectForm(instance = project)
        return render(request, 'update_project.html', {
            'project': project,
            'form': form
        })
    else:
        project = Project.objects.get(id=project_id)
        form = CreateProjectForm(request.POST, instance=project)
        form.save()
        return redirect('projects')

def update_task(request, task_id):
    if request.method == 'GET':
        task = Task.objects.get(id=task_id)
        form = CreateTaskForm(instance = task)
        return render(request, 'update_task.html', {
            'task': task,
            'form': form
        })
    else:
        
        task = Task.objects.get(id=task_id)
        form = CreateTaskForm(request.POST, instance=task)
        form.save()
        return redirect('project_view', task.project_id)