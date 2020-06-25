from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Project
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .form import ProjectForm
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect



class ProjectsListView(LoginRequiredMixin, ListView):
    model = Project
    context_object_name = 'projects'
    template_name = 'projects.html'

class ProjectDetailView(LoginRequiredMixin, DetailView):
    model = Project
    context_object_name = 'project'
    template_name = 'project.html'
    slug_field = 'project_slug'


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    template_name = 'project/new_project.html'
    fields = '__all__'



@login_required
def projects_filter(request, status):
    projects = Project.objects.filter(project_status = status)
    return render(request, 'projects.html', {'projects': projects})


# @login_required
# def projects(request):
#     projects = Project.objects.all()
#     return render(request, 'projects.html', {'projects': projects})




# @login_required
# def project(request, slug):
#     project = get_object_or_404(Project, project_slug=slug)
#     return render(request,'project.html', {'project':project})



# @login_required
# def create_project(request):
#     new_project = False
#     if request.method == 'POST':
#         project_form = ProjectForm(data=request.POST)
#         if project_form.is_valid():
#             new_project = project_form.save()
#             new_project = True
#             return HttpResponseRedirect("/project/")
#     else:
#         project_form = ProjectForm()
#     return render(request, 'project/new_project.html', {'new_project': new_project,
#                                                                   'form': project_form})