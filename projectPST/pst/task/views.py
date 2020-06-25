from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .form import TaskForm
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect



class TasksListView(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'tasks.html'

class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'task.html'
    pk_url_kwarg = "id"


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = 'task/new_task.html'
    fields = '__all__'

@login_required
def tasks_filter(request, status):
    tasks = Task.objects.filter(task_status = status)
    return render(request, 'tasks.html', {'tasks': tasks})



# @login_required
# def tasks(request):
#     tasks = Task.objects.all()
#     return render(request,'tasks.html',{'tasks':tasks})




# @login_required
# def task(request, slug, id):
#     task = get_object_or_404(Task, task_slug=slug, id = id)
#     return render(request,'task.html', {'task':task, 'id':id})


# @login_required
# def create_task(request):
#     new_task = False
#     if request.method == 'POST':
#         task_form = TaskForm(data=request.POST)
#         if task_form.is_valid():
#             new_task =task_form.save()
#             new_task = True
#             return HttpResponseRedirect("/task/")
#     else:
#         task_form = TaskForm()
#     return render(request, 'task/new_task.html', {'new_task': new_task,
#                                                                   'form': task_form})

