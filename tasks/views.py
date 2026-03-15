from django.shortcuts import render, redirect
from .models import Task
from django.contrib.auth.decorators import login_required

@login_required
def task_list(request):
   
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

@login_required
def create_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
      
        Task.objects.create(user=request.user, title=title, description=description)
        return redirect('tasks')
    return render(request, 'tasks/task_form.html')

@login_required
def delete_task(request, pk):
    task = Task.objects.get(id=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('tasks')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})

@login_required
def toggle_task(request, pk):

    task = Task.objects.get(id=pk)
    task.complete = not task.complete 
    task.save()
    return redirect('tasks')