from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Step
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .form import StepForm
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect


class StepsListView(LoginRequiredMixin, ListView):
    model = Step
    context_object_name = 'steps'
    template_name = 'steps.html'


class StepDetailView(LoginRequiredMixin, DetailView):
    model = Step
    context_object_name = 'step'
    template_name = 'step.html'
    pk_url_kwarg = "id"

class StepCreateView(LoginRequiredMixin, CreateView):
    model = Step
    template_name = 'step/new_step.html'
    fields = '__all__'

@login_required
def steps_filter(request, status):
    steps = Step.objects.filter(step_status = status)
    return render(request, 'steps.html', {'steps': steps})

# @login_required
# def steps(request):
#     steps = Step.objects.all()
#     return render(request,'steps.html',{'steps':steps})


# @login_required
# def step(request, slug, id):
#     step = get_object_or_404(Step, step_slug=slug, id = id)
#     return render(request,'step.html', {'step':step, 'id':id})


# @login_required
# def create_step(request):
#     new_step = False
#     if request.method == 'POST':
#         step_form = StepForm(data=request.POST)
#         if step_form.is_valid():
#             new_step = step_form.save()
#             new_step = True
#             return HttpResponseRedirect("/step/")
#     else:
#         step_form = StepForm()
#     return render(request, 'step/new_step.html', {'new_step': new_step,
#                                                                   'form': step_form})

