from django.contrib import admin
from .models import Step
from task.models import Task

class TaskInline(admin.TabularInline):
    model = Task
    extra = 0


@admin.register(Step)
class StepAdmin(admin.ModelAdmin):
    fields =        (
                    'step_project',
                    'step_name',
                    'step_slug',
                     ('step_specification_short',
                    'step_specification_full'),
                    'step_status',
                    ('step_date_start',
                    'step_date_finish')
                    )
    list_display = (
                    'step_project',
                    'step_name',
                    # 'step_slug',
                    # 'step_specification_short',
                    # 'step_specification_full',
                    'step_status',
                    # 'step_date_created',
                    'step_date_start',
                    'step_date_finish'
                    )
    list_editable = ('step_status',)
    list_filter = (
                    'step_project',
                   'step_status',
                    )
    search_fields = (
                      'step_specification_short',
                    )
    prepopulated_fields = {'step_slug':('step_name',)}
    ordering = (
                'step_project',
                'step_status',
                'step_date_start',
                )
    inlines = [
        TaskInline,
    ]